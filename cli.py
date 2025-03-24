# cli.py
import os
import sys
import pandas as pd
from utils.preprocessing import clean_resume
from models.sentence_transformer_model import encode_text
from utils.ranking import compute_similarity


def load_resumes():
    """Load resumes from the dataset"""
    try:
        df = pd.read_csv("data/UpdatedResumeDataSet.csv", encoding="utf-8")
        print(f"Loaded {len(df)} resumes from dataset")
        return df
    except Exception as e:
        print(f"Error loading resume dataset: {e}")
        sys.exit(1)


def get_job_description():
    """Prompt the user to input a job description"""
    print("Please enter the job description (hit Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    job_description = "\n".join(lines)

    if not job_description.strip():
        print("Job description cannot be empty!")
        return get_job_description()
    return job_description


def get_resume_from_file():
    """Allow the user to upload a resume text file"""
    print("Enter the resume file path (.txt file):")
    file_path = input()
    if not os.path.exists(file_path):
        print("File does not exist!")
        return get_resume_from_file()

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            resume_text = file.read()
        if not resume_text.strip():
            print("Resume file is empty!")
            return get_resume_from_file()
        return resume_text
    except Exception as e:
        print(f"Error reading file: {e}")
        return get_resume_from_file()


def display_top_resumes(df_sorted, num=5):
    """Display the top ranked resumes based on similarity"""
    print(f"\nTop {num} Resumes (Ranked by Similarity to Job Description):\n")
    for i, row in df_sorted.head(num).iterrows():
        print(f"Rank {i + 1}:")
        print(f"Score: {row['Score']:.4f}")
        # Display a snippet of the resume to avoid overwhelming output
        resume_snippet = row['Cleaned_Resume'][:200] + "..." if len(row['Cleaned_Resume']) > 200 else row[
            'Cleaned_Resume']
        print(f"Resume snippet: {resume_snippet}\n")


def filter_resumes_by_category(df):
    """Allow user to filter resumes by category"""
    categories = df['Category'].unique()
    print("\nAvailable resume categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    print("\nSelect a category number (or press Enter to use all categories):")
    choice = input()

    if choice.strip():
        try:
            category_idx = int(choice) - 1
            if 0 <= category_idx < len(categories):
                selected_category = categories[category_idx]
                filtered_df = df[df['Category'] == selected_category]
                print(f"Filtered to {len(filtered_df)} resumes in category: {selected_category}")
                return filtered_df
            else:
                print("Invalid selection. Using all categories.")
                return df
        except ValueError:
            print("Invalid input. Using all categories.")
            return df
    return df


def main():
    """Main function to run the CLI interface"""
    try:
        print("\n===== Resume Matcher CLI =====\n")

        # Step 1: Load resumes from dataset
        df = load_resumes()

        # Optional: Filter by category
        df = filter_resumes_by_category(df)

        # Step 2: Get job description from user
        job_desc = get_job_description()
        print("\nProcessing job description...")
        job_vec = encode_text(job_desc)

        # Step 3: Ask the user to upload a resume file
        print("\n== Upload your resume to compare with job description ==")
        resume_text = get_resume_from_file()

        # Step 4: Preprocess and clean resume text
        print("\nPreprocessing resume...")
        cleaned_resume = clean_resume(resume_text)

        # Step 5: Generate vector for the resume
        resume_vec = encode_text(cleaned_resume)

        # Step 6: Compute similarity
        similarity_score = compute_similarity(job_vec, resume_vec)

        # Step 7: Display results for uploaded resume
        print(f"\n== Results ==")
        print(f"Similarity Score for your resume: {similarity_score:.4f}")

        # Interpret the score
        if similarity_score > 0.7:
            print("Great match! Your resume aligns well with the job description.")
        elif similarity_score > 0.5:
            print("Good match. Consider highlighting relevant skills more prominently.")
        else:
            print("Low match. You might want to tailor your resume more for this position.")

        # Step 8: Process dataset resumes for comparison
        print("\nComparing with other resumes in the dataset...")
        df["Cleaned_Resume"] = df["Resume"].apply(clean_resume)
        df["Score"] = df["Cleaned_Resume"].apply(lambda x: compute_similarity(job_vec, encode_text(x)))
        df_sorted = df.sort_values(by="Score", ascending=False)

        # Step 9: Display top resumes from the dataset
        display_top_resumes(df_sorted)

    except KeyboardInterrupt:
        print("\nOperation canceled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")


if __name__ == "__main__":
    main()