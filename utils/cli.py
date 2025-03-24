# cli.py
import os
import sys
import pandas as pd
from utils.preprocessing import clean_resume
from models.sentence_transformer_model import encode_text
from utils.ranking import compute_similarity


def load_resumes():
    """Load resumes from the dataset"""
    # You can use the dataset you have or ask the user to upload resumes manually
    df = pd.read_csv("data/UpdatedResumeDataSet.csv")
    return df


def get_job_description():
    """Prompt the user to input a job description"""
    print("Please enter the job description:")
    job_description = input()
    return job_description


def get_resume_from_file():
    """Allow the user to upload a resume file (e.g., txt or pdf)"""
    print("Enter the resume file path:")
    file_path = input()
    if not os.path.exists(file_path):
        print("File does not exist!")
        sys.exit()
    with open(file_path, 'r') as file:
        resume_text = file.read()
    return resume_text


def display_top_resumes(df_sorted):
    """Display the top 5 ranked resumes based on similarity"""
    print("\nTop 5 Resumes (Ranked by Similarity to Job Description):\n")
    for i, row in df_sorted.head(5).iterrows():
        print(f"Rank {i + 1}:")
        print(f"Score: {row['Score']}")
        print(f"Resume: {row['Cleaned_Resume']}\n")


def main():
    """Main function to run the CLI interface"""
    # Step 1: Load resumes from dataset (or file system)
    df = load_resumes()

    # Step 2: Get job description from user
    job_desc = get_job_description()
    job_vec = encode_text(job_desc)  # Encode job description into vector

    # Step 3: Ask the user to upload a resume file
    resume_text = get_resume_from_file()  # Get resume from file

    # Step 4: Preprocess and clean resume text
    cleaned_resume = clean_resume(resume_text)

    # Step 5: Generate vector for the resume
    resume_vec = encode_text(cleaned_resume)

    # Step 6: Compute similarity between job description and the uploaded resume
    similarity_score = compute_similarity(job_vec, resume_vec)

    # Step 7: Display results
    print(f"\nSimilarity Score for the uploaded resume: {similarity_score:.4f}\n")

    # Display top resumes from dataset (if needed)
    df["Cleaned_Resume"] = df["Resume"].apply(clean_resume)
    df["Score"] = df["Cleaned_Resume"].apply(lambda x: compute_similarity(job_vec, encode_text(x)))
    df_sorted = df.sort_values(by="Score", ascending=False)
    display_top_resumes(df_sorted)


if __name__ == "__main__":
    main()