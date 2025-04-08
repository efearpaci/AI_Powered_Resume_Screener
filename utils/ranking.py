import torch
from models.sentence_transformer_model import encode_text
# Define a dictionary of role-specific required skills
ROLE_SKILLS = {
    "data science": ["python", "machine learning", "data analysis", "sql", "tensorflow", "pytorch", "r", "statistics"],
    "web designing": ["html", "css", "javascript", "react", "angular", "ux", "ui", "bootstrap", "photoshop"],
    "java developer": ["java", "spring", "hibernate", "maven", "j2ee", "servlets", "jsp"],
    "automation testing": ["selenium", "cucumber", "qa", "test automation", "appium", "junit", "pytest"],
    "python developer": ["python", "django", "flask", "rest", "api", "pandas", "numpy", "sql"],
    "network security engineer": ["network security", "firewall", "vpn", "cryptography", "penetration testing", "ids", "ips", "wireshark"]
}
def compute_skill_overlap(job_desc, resume_text, skills):
    """
    Compute an overlap score for the given skills.
    Returns a fraction (0 to 1) representing the proportion of required skills
    that appear in both the job description and the resume.
    """
    job_desc_lower = job_desc.lower()
    resume_text_lower = resume_text.lower()
    matching = [skill for skill in skills if skill in job_desc_lower and skill in resume_text_lower]
    return len(matching) / len(skills) if skills else 0.0

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
            self.model.eval()  # Set the model to evaluation mode to disable dropout
            self.initialized = True
        except Exception as e:
            print(f"Error loading transformer model: {e}")
            self.initialized = False

    def compute_relevance(self, job_desc, resume_text, job_category="default"):
        if not self.initialized:
            return standard_ranking(job_desc, resume_text)

        from utils.preprocessing import clean_resume
        cleaned_job = clean_resume(job_desc) if job_desc else ""
        cleaned_resume = clean_resume(resume_text) if resume_text else ""

        inputs = self.tokenizer(cleaned_job, cleaned_resume, return_tensors="pt",
                                padding=True, truncation=True, max_length=512)

        with torch.no_grad():
            outputs = self.model(**inputs)

        # Get logits from the output (assume binary classification)
        logits = outputs.logits[0]
        if logits.shape[0] >= 2:
            prob = torch.softmax(logits, dim=0)[1].item()
        else:
            prob = torch.sigmoid(logits).item()

        # Semantic score (using the raw probability)
        semantic_score = max(0, min(1, prob))  # No extra scaling

        # Select required skills based on the job category
        try:
            job_category_lc = job_category.lower()
        except Exception:
            job_category_lc = ""
        if job_category_lc in ROLE_SKILLS:
            required_skills = ROLE_SKILLS[job_category_lc]
        else:
            # Fallback: use a broader general IT skills list
            required_skills = [
                "python", "java", "c++", "c#", "javascript", "sql", "nosql",
                "machine learning", "data analysis", "blockchain", "testing", "devops",
                "cloud", "docker", "kubernetes", "tensorflow", "pytorch", "database",
                "networking", "security", "angular", "react", "node"
            ]

        # Compute skill overlap score
        skill_score = compute_skill_overlap(job_desc, resume_text, required_skills)

        # Combine semantic and skill scores (70% semantic, 30% skill)
        combined_score = 0.7 * semantic_score + 0.3 * skill_score

        return combined_score


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