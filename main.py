job_desc = """
We are looking for a Data Scientist with experience in Python, machine learning,
data analysis, SQL, and deep learning frameworks such as TensorFlow or PyTorch.

We are looking for a Software Testing Engineer to join our quality assurance team. 
You will be responsible for ensuring the reliability and performance of our software 
products through rigorous testing and analysis.

We are seeking a Blockchain Developer with a strong background in developing decentralized applications
and smart contracts. You will be involved in building secure and scalable blockchain solutions
for various business applications.

We are looking for a skilled Database Administrator/Engineer to manage and optimize
our enterprise data systems. You will ensure the integrity, performance, and security of
our databases to support data-driven applications.
"""

import pandas as pd
from utils.preprocessing import clean_resume
from models.sentence_transformer_model import encode_text
from utils.ranking import compute_similarity

df = pd.read_csv("data/UpdatedResumeDataSet.csv", encoding ="utf-8")
df = df[df["Category"] == "Data Science"]

df["Cleaned_Resume"] = df["Resume"].apply(clean_resume)

job_vec = encode_text(job_desc)

df["Score"] = df["Cleaned_Resume"].apply(lambda x: compute_similarity(job_vec, encode_text(x)))

df_sorted = df.sort_values(by="Score", ascending=False)
df_sorted = df_sorted.drop_duplicates(subset=["Resume"], keep="first")

print(df_sorted[["Score", "Resume"]].head(5))