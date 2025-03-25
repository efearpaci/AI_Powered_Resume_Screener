import os
import sys
import pandas as pd
from utils.preprocessing import clean_resume
from models.sentence_transformer_model import encode_text
from utils.ranking import compute_similarity


def load_resumes():
    try:
        df = pd.read_csv("data/UpdatedResumeDataSet.csv", encoding="utf-8")
        print(f"Loaded {len(df)} resumes from dataset")
        return df
    except Exception as e:
        print(f"Error loading resume dataset: {e}")
        sys.exit(1)


def get_job_description():
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
    print(f"\nTop {num} Resumes (Ranked by Similarity to Job Description):\n")
    for i, row in df_sorted.head(num).iterrows():
        print(f"Rank {i + 1}:")
        print(f"Score: {row['Score']:.4f}")
        resume_snippet = row['Cleaned_Resume'][:200] + "..." if len(row['Cleaned_Resume']) > 200 else row[
            'Cleaned_Resume']
        print(f"Resume snippet: {resume_snippet}\n")


def filter_resumes_by_category(df):
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
    try:
        print("\n===== Resume Matcher CLI =====\n")

        df = load_resumes()

        df = filter_resumes_by_category(df)

        job_desc = get_job_description()
        print("\nProcessing job description...")
        job_vec = encode_text(job_desc)

        print("\n== Upload your resume to compare with job description ==")
        resume_text = get_resume_from_file()

        print("\nPreprocessing resume...")
        cleaned_resume = clean_resume(resume_text)

        resume_vec = encode_text(cleaned_resume)

        similarity_score = compute_similarity(job_vec, resume_vec)

        print(f"\n== Results ==")
        print(f"Similarity Score for your resume: {similarity_score:.4f}")

        if similarity_score > 0.7:
            print("Great match! Your resume aligns well with the job description.")
        elif similarity_score > 0.5:
            print("Good match. Consider highlighting relevant skills more prominently.")
        else:
            print("Low match. You might want to tailor your resume more for this position.")

        print("\nComparing with other resumes in the dataset...")
        df["Cleaned_Resume"] = df["Resume"].apply(clean_resume)
        df["Score"] = df["Cleaned_Resume"].apply(lambda x: compute_similarity(job_vec, encode_text(x)))
        df_sorted = df.sort_values(by="Score", ascending=False)

        display_top_resumes(df_sorted)

    except KeyboardInterrupt:
        print("\nOperation canceled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")


if __name__ == "__main__":
    main()