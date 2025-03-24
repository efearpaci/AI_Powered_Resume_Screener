from sentence_transformers import util

def compute_similarity(job_vec, resume_vec):
    return util.pytorch_cos_sim(job_vec, resume_vec).item()