job_desc = """
We are looking for a Data Scientist with experience in Python, machine learning,
data analysis, SQL, and deep learning frameworks such as TensorFlow or PyTorch.
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

print(df_sorted[["Score", "Resume"]].head(5))