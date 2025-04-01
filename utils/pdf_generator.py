from fpdf import FPDF

# ------------------------------
# Sample Resume 1 - Strong Match
# ------------------------------
pdf1 = FPDF()
pdf1.add_page()
pdf1.set_font("Arial", 'B', 16)
pdf1.cell(0, 10, "Data Scientist Resume - Candidate 1", ln=True, align="C")
pdf1.ln(10)
pdf1.set_font("Arial", '', 12)
pdf1.cell(0, 10, "Name: Alice Johnson", ln=True)
pdf1.cell(0, 10, "Email: alice.johnson@example.com", ln=True)
pdf1.cell(0, 10, "Phone: 123-456-7890", ln=True)
pdf1.ln(10)
pdf1.set_font("Arial", 'B', 14)
pdf1.cell(0, 10, "Summary", ln=True)
pdf1.set_font("Arial", '', 12)
pdf1.multi_cell(0, 10,
    "Experienced Data Scientist with a strong background in Python, machine learning, data analysis, SQL, "
    "and deep learning frameworks such as TensorFlow and PyTorch. Proven expertise in developing and deploying "
    "predictive models and delivering actionable insights from complex datasets."
)
pdf1.ln(10)
pdf1.set_font("Arial", 'B', 14)
pdf1.cell(0, 10, "Skills", ln=True)
pdf1.set_font("Arial", '', 12)
pdf1.multi_cell(0, 10, "Python, Machine Learning, Data Analysis, SQL, TensorFlow, PyTorch, Pandas, Scikit-learn")
pdf1.ln(10)
pdf1.set_font("Arial", 'B', 14)
pdf1.cell(0, 10, "Experience", ln=True)
pdf1.set_font("Arial", '', 12)
pdf1.multi_cell(0, 10,
    "Data Scientist at TechCorp (2020-2023): Developed and deployed predictive models, implemented data analysis pipelines, "
    "and collaborated with cross-functional teams to drive strategic business insights."
)
pdf1.output("sample_resume_candidate1.pdf")

# -------------------------------
# Sample Resume 2 - Moderate Match
# -------------------------------
pdf2 = FPDF()
pdf2.add_page()
pdf2.set_font("Arial", 'B', 16)
pdf2.cell(0, 10, "Data Scientist Resume - Candidate 2", ln=True, align="C")
pdf2.ln(10)
pdf2.set_font("Arial", '', 12)
pdf2.cell(0, 10, "Name: Bob Smith", ln=True)
pdf2.cell(0, 10, "Email: bob.smith@example.com", ln=True)
pdf2.cell(0, 10, "Phone: 987-654-3210", ln=True)
pdf2.ln(10)
pdf2.set_font("Arial", 'B', 14)
pdf2.cell(0, 10, "Summary", ln=True)
pdf2.set_font("Arial", '', 12)
pdf2.multi_cell(0, 10,
    "Motivated Data Scientist with practical experience in Python and data analysis, with working knowledge of SQL. "
    "Familiar with TensorFlow and basic machine learning techniques, seeking to further develop expertise in advanced models."
)
pdf2.ln(10)
pdf2.set_font("Arial", 'B', 14)
pdf2.cell(0, 10, "Skills", ln=True)
pdf2.set_font("Arial", '', 12)
pdf2.multi_cell(0, 10, "Python, Data Analysis, SQL, TensorFlow, Basic Machine Learning, R")
pdf2.ln(10)
pdf2.set_font("Arial", 'B', 14)
pdf2.cell(0, 10, "Experience", ln=True)
pdf2.set_font("Arial", '', 12)
pdf2.multi_cell(0, 10,
    "Data Analyst at DataWorks (2019-2022): Analyzed datasets, generated actionable insights, and supported business decisions "
    "through data-driven analysis."
)
pdf2.output("sample_resume_candidate2.pdf")
from fpdf import FPDF

# Create a new PDF instance for a "bad" resume
pdf_bad = FPDF()
pdf_bad.add_page()
pdf_bad.set_font("Arial", 'B', 16)
pdf_bad.cell(0, 10, "Bad Resume - Candidate: John Doe", ln=True, align="C")
pdf_bad.ln(10)

# Contact details (poorly formatted and uninformative)
pdf_bad.set_font("Arial", '', 12)
pdf_bad.cell(0, 10, "Name: John Doe", ln=True)
pdf_bad.cell(0, 10, "Email: johndoe@example.com", ln=True)
pdf_bad.cell(0, 10, "Phone: 000-000-0000", ln=True)
pdf_bad.ln(10)

# Summary: vague and irrelevant content
pdf_bad.set_font("Arial", 'B', 14)
pdf_bad.cell(0, 10, "Summary", ln=True)
pdf_bad.set_font("Arial", '', 12)
pdf_bad.multi_cell(0, 10,
    "I like computers but don't really know much about data science. "
    "I sometimes write code, but it rarely works. Not really sure what machine learning is. "
    "I enjoy watching TV and playing games, and I have little interest in technical challenges."
)
pdf_bad.ln(10)

# Skills: almost none or irrelevant skills
pdf_bad.set_font("Arial", 'B', 14)
pdf_bad.cell(0, 10, "Skills", ln=True)
pdf_bad.set_font("Arial", '', 12)
pdf_bad.multi_cell(0, 10, "None, basic computer usage, occasional code errors")
pdf_bad.ln(10)

# Experience: irrelevant or low-quality experience
pdf_bad.set_font("Arial", 'B', 14)
pdf_bad.cell(0, 10, "Experience", ln=True)
pdf_bad.set_font("Arial", '', 12)
pdf_bad.multi_cell(0, 10,
    "Worked at a local cafe for 1 year. Had a part-time job that did not involve any programming or data analysis. "
    "No experience related to data science or technical roles."
)
pdf_bad.output("bad_resume.pdf")

print("Bad resume PDF generated as 'bad_resume.pdf'")

print("Sample resume PDFs generated:")
print(" - sample_resume_candidate1.pdf")
print(" - sample_resume_candidate2.pdf")