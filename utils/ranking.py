import torch
from models.sentence_transformer_model import encode_text


def compute_similarity(vec1, vec2):
    if torch.is_tensor(vec1) and torch.is_tensor(vec2):
        cos_sim = torch.nn.functional.cosine_similarity(vec1.unsqueeze(0), vec2.unsqueeze(0))
        return cos_sim.item()
    return 0.0


class AdvancedRankingModel:
    def __init__(self, model_name="bert-base-uncased"):
        try:
            from transformers import AutoTokenizer, AutoModelForSequenceClassification
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
            self.initialized = True
        except Exception as e:
            print(f"Error loading transformer model: {e}")
            self.initialized = False

    def compute_relevance(self, job_desc, resume_text):
        if not self.initialized:
            return standard_ranking(job_desc, resume_text)

        from utils.preprocessing import clean_resume
        cleaned_job = clean_resume(job_desc) if job_desc else ""
        cleaned_resume = clean_resume(resume_text) if resume_text else ""

        inputs = self.tokenizer(cleaned_job, cleaned_resume, return_tensors="pt",
                                padding=True, truncation=True, max_length=512)

        with torch.no_grad():
            outputs = self.model(**inputs)

        if hasattr(outputs, 'logits') and outputs.logits.shape[1] >= 2:
            score = torch.softmax(outputs.logits, dim=1)[0][1].item()
        else:
            score = torch.sigmoid(outputs.logits[0]).item()

        return score


def standard_ranking(job_desc, resume_text):
    from utils.preprocessing import clean_resume
    cleaned_job = clean_resume(job_desc) if job_desc else ""
    cleaned_resume = clean_resume(resume_text) if resume_text else ""

    job_vec = encode_text(cleaned_job)
    resume_vec = encode_text(cleaned_resume)
    return compute_similarity(job_vec, resume_vec)


_advanced_model = None


def get_ranking_method(method="standard"):
    global _advanced_model

    if method == "advanced":
        try:
            if _advanced_model is None:
                _advanced_model = AdvancedRankingModel()
            return _advanced_model.compute_relevance
        except Exception as e:
            print(f"Failed to initialize advanced ranking: {e}")
            return standard_ranking
    else:
        return standard_ranking