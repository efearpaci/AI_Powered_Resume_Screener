import os
import sys
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import pandas as pd
import threading
import warnings
import logging

logging.basicConfig(level=logging.WARNING)

class ResumeMatcherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Powered Resume Screener")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)

        self.df = None
        self.job_vec = None
        self.resume_path = None

        self.create_widgets()
        self.load_dataset()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        job_frame = ttk.LabelFrame(main_frame, text="Job Description", padding=10)
        job_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.job_text = scrolledtext.ScrolledText(job_frame, wrap=tk.WORD, height=8)
        self.job_text.pack(fill=tk.BOTH, expand=True)

        resume_frame = ttk.LabelFrame(main_frame, text="Resume", padding=10)
        resume_frame.pack(fill=tk.BOTH, expand=False, pady=5)

        resume_btn_frame = ttk.Frame(resume_frame)
        resume_btn_frame.pack(fill=tk.X)

        self.resume_path_var = tk.StringVar()
        self.resume_path_var.set("No file selected")

        ttk.Button(resume_btn_frame, text="Browse Resume", command=self.browse_resume).pack(side=tk.LEFT, padx=5)
        ttk.Label(resume_btn_frame, textvariable=self.resume_path_var).pack(side=tk.LEFT, padx=5, fill=tk.X,
                                                                            expand=True)

        category_frame = ttk.LabelFrame(main_frame, text="Category Filter", padding=10)
        category_frame.pack(fill=tk.X, pady=5)

        self.category_var = tk.StringVar()
        self.category_var.set("All Categories")
        self.category_dropdown = ttk.Combobox(category_frame, textvariable=self.category_var, state="readonly")
        self.category_dropdown.pack(fill=tk.X)

        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=10)

        ttk.Button(btn_frame, text="Calculate scores", command=self.find_matches).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_fields).pack(side=tk.LEFT, padx=5)

        self.progress_var = tk.DoubleVar()
        self.progress = ttk.Progressbar(main_frame, variable=self.progress_var, maximum=100)
        self.progress.pack(fill=tk.X, pady=5)

        results_frame = ttk.LabelFrame(main_frame, text="Results", padding=10)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.match_quality_var = tk.StringVar()
        ttk.Label(results_frame, textvariable=self.match_quality_var).pack(anchor=tk.W, pady=5)

        ttk.Label(results_frame, text="Top Matches from Dataset:").pack(anchor=tk.W, pady=5)

        columns = ("Rank", "Score", "Resume Snippet")
        self.results_tree = ttk.Treeview(results_frame, columns=columns, show="headings", height=10)

        for col in columns:
            self.results_tree.heading(col, text=col)

        self.results_tree.column("Rank", width=50, anchor=tk.CENTER)
        self.results_tree.column("Score", width=100, anchor=tk.CENTER)
        self.results_tree.column("Resume Snippet", width=600)

        self.results_tree.pack(fill=tk.BOTH, expand=True)
        self.results_tree.bind("<Double-1>", self.open_resume_details)


        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def load_dataset(self):
        try:
            self.status_var.set("Loading resume dataset...")
            self.df = pd.read_csv("data/UpdatedResumeDataSet.csv", encoding="utf-8")

            categories = ["All Categories"] + list(self.df['Category'].unique())
            self.category_dropdown['values'] = categories

            self.status_var.set(f"Loaded {len(self.df)} resumes from dataset")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load resume dataset: {str(e)}")
            self.status_var.set("Error loading dataset")

    def browse_resume(self):
        file_path = filedialog.askopenfilename(
            title="Select Resume File",
            filetypes=[("Text files", "*.txt"), ("PDF files", "*.pdf"), ("Word files", "*.docx"), ("All files", "*.*")]
        )

        if file_path:
            self.resume_path = file_path
            self.resume_path_var.set(os.path.basename(file_path))

    def clear_fields(self):
        self.job_text.delete(1.0, tk.END)
        self.resume_path = None
        self.resume_path_var.set("No file selected")
        self.category_var.set("All Categories")
        self.match_quality_var.set("")

        for item in self.results_tree.get_children():
            self.results_tree.delete(item)

    def find_matches(self):
        job_desc = self.job_text.get(1.0, tk.END).strip()
        if not job_desc:
            messagebox.showwarning("Warning", "Please enter a job description")
            return

        if not self.resume_path:
            messagebox.showwarning("Warning", "Please select a resume file")
            return

        threading.Thread(target=self.process_matching, daemon=True).start()

    def open_resume_details(self, event):
        selected_item = self.results_tree.selection()
        if not selected_item:
            return

        item_values = self.results_tree.item(selected_item[0], "values")
        rank = int(item_values[0]) - 1

        selected_category = self.category_var.get()
        working_df = self.df.copy()

        if selected_category != "All Categories":
            working_df = working_df[working_df["Category"] == selected_category]

        job_desc = self.job_text.get(1.0, tk.END).strip()
        from utils.ranking import get_ranking_method
        ranking_method = get_ranking_method("advanced")

        working_df["Score"] = working_df["Resume"].apply(
            lambda x: ranking_method(job_desc, x)
        )
        df_sorted = working_df.sort_values(by="Score", ascending=False)

        if rank < len(df_sorted):
            resume_text = df_sorted.iloc[rank]["Resume"]

            resume_window = tk.Toplevel(self.root)
            resume_window.title(f"Resume Details - Rank #{rank + 1}")
            resume_window.geometry("700x500")

            frame = ttk.Frame(resume_window, padding=10)
            frame.pack(fill=tk.BOTH, expand=True)

            resume_display = scrolledtext.ScrolledText(frame, wrap=tk.WORD)
            resume_display.pack(fill=tk.BOTH, expand=True)
            resume_display.insert(tk.END, resume_text)
            resume_display.config(state=tk.DISABLED)  # Make it read-only

            ttk.Button(frame, text="Close", command=resume_window.destroy).pack(pady=10)

    def process_matching(self):
        try:
            self.status_var.set("Processing...")
            self.progress_var.set(10)
            job_desc = self.job_text.get(1.0, tk.END).strip()
            if not job_desc:
                self.status_var.set("Please enter a job description")
                return

            from utils.ranking import get_ranking_method
            ranking_method = get_ranking_method("advanced")
            ext = os.path.splitext(self.resume_path)[1].lower()

            if ext == ".csv":
                # Process uploaded CSV file to get top 10 matches from dataset
                import pandas as pd
                try:
                    uploaded_df = pd.read_csv(self.resume_path, encoding='utf-8')
                except Exception as e:
                    self.root.after(0, lambda: messagebox.showerror("Error", f"Error reading CSV file: {str(e)}"))
                    self.status_var.set("Error reading CSV file")
                    return

                # Optional: Filter by category if applicable
                selected_category = self.category_var.get()
                if selected_category != "All Categories":
                    uploaded_df = uploaded_df[uploaded_df["Category"] == selected_category]

                self.progress_var.set(30)
                uploaded_df["Score"] = uploaded_df["Resume"].apply(lambda x: ranking_method(job_desc, x))
                self.progress_var.set(90)
                df_sorted = uploaded_df.sort_values(by="Score", ascending=False)
                df_sorted = df_sorted.drop_duplicates(subset=["Resume"], keep="first")

                self.root.after(0,
                                lambda: [self.results_tree.delete(item) for item in self.results_tree.get_children()])
                for idx, (_, row) in enumerate(df_sorted.head(10).iterrows()):
                    resume_snippet = row['Resume'][:200] + "..." if len(row['Resume']) > 200 else row['Resume']
                    self.root.after(0, lambda idx=idx, score=row['Score'], snippet=resume_snippet:
                    self.results_tree.insert("", tk.END, values=(idx + 1, f"{score:.4f}", snippet)))
                self.root.after(0, lambda: self.match_quality_var.set(""))
                self.progress_var.set(100)
                self.status_var.set("Matching complete")
            else:
                # Process single resume file (txt, pdf, docx)
                try:
                    from utils.resume_reader import read_resume
                    resume_text = read_resume(self.resume_path)
                except Exception as e:
                    self.root.after(0, lambda: messagebox.showerror("Error", f"Error reading resume file: {str(e)}"))
                    self.status_var.set("Error reading resume file")
                    return

                self.progress_var.set(50)
                similarity_score = ranking_method(job_desc, resume_text)
                self.progress_var.set(70)
                if similarity_score > 0.7:
                    quality_text = "Great match! Your resume aligns well with the job description."
                elif similarity_score > 0.5:
                    quality_text = "Good match. Consider highlighting relevant skills more prominently."
                else:
                    quality_text = "Low match. You might want to tailor your resume more for this position."

                self.root.after(0,
                                lambda: self.match_quality_var.set(quality_text + f" (Score: {similarity_score:.4f})"))
                self.root.after(0,
                                lambda: [self.results_tree.delete(item) for item in self.results_tree.get_children()])
                self.progress_var.set(100)
                self.status_var.set("Matching complete")
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"An error occurred: {str(e)}"))
            self.status_var.set("Error during processing")
        finally:
            self.root.after(2000, lambda: self.progress_var.set(0))


def main():
    root = tk.Tk()
    app = ResumeMatcherGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()