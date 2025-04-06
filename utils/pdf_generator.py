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

from fpdf import FPDF

# ------------- Testing Category: Good Match -------------
pdf_test_good = FPDF()
pdf_test_good.add_page()
pdf_test_good.set_font("Arial", 'B', 16)
pdf_test_good.cell(0, 10, "Testing Engineer Resume - Good Match", ln=True, align="C")
pdf_test_good.ln(10)
pdf_test_good.set_font("Arial", '', 12)
pdf_test_good.cell(0, 10, "Name: Sarah Tester", ln=True)
pdf_test_good.cell(0, 10, "Email: sarah.tester@example.com", ln=True)
pdf_test_good.cell(0, 10, "Phone: 555-123-4567", ln=True)
pdf_test_good.ln(10)
pdf_test_good.set_font("Arial", 'B', 14)
pdf_test_good.cell(0, 10, "Summary", ln=True)
pdf_test_good.set_font("Arial", '', 12)
pdf_test_good.multi_cell(0, 10,
    "Experienced Testing Engineer with strong skills in both manual and automated testing. Proficient in Selenium, JIRA, "
    "and Agile methodologies. Consistently ensures software quality by identifying and resolving bugs efficiently."
)
pdf_test_good.ln(10)
pdf_test_good.set_font("Arial", 'B', 14)
pdf_test_good.cell(0, 10, "Skills", ln=True)
pdf_test_good.set_font("Arial", '', 12)
pdf_test_good.multi_cell(0, 10, "Manual Testing, Automated Testing, Selenium, JIRA, Agile, TestRail")
pdf_test_good.ln(10)
pdf_test_good.set_font("Arial", 'B', 14)
pdf_test_good.cell(0, 10, "Experience", ln=True)
pdf_test_good.set_font("Arial", '', 12)
pdf_test_good.multi_cell(0, 10,
    "Testing Engineer at QualitySoft (2018-2023): Developed and executed automated test scripts, "
    "improved test coverage by 30%, and collaborated with developers to enhance product quality."
)
pdf_test_good.output("sample_resume_testing_good.pdf")

# ------------- Testing Category: Bad Match -------------
pdf_test_bad = FPDF()
pdf_test_bad.add_page()
pdf_test_bad.set_font("Arial", 'B', 16)
pdf_test_bad.cell(0, 10, "Testing Engineer Resume - Bad Match", ln=True, align="C")
pdf_test_bad.ln(10)
pdf_test_bad.set_font("Arial", '', 12)
pdf_test_bad.cell(0, 10, "Name: Mark Ineffective", ln=True)
pdf_test_bad.cell(0, 10, "Email: mark.ineffective@example.com", ln=True)
pdf_test_bad.cell(0, 10, "Phone: 555-987-6543", ln=True)
pdf_test_bad.ln(10)
pdf_test_bad.set_font("Arial", 'B', 14)
pdf_test_bad.cell(0, 10, "Summary", ln=True)
pdf_test_bad.set_font("Arial", '', 12)
pdf_test_bad.multi_cell(0, 10,
    "Unfocused individual with little to no experience in software testing. Lacks familiarity with testing tools "
    "and methodologies, often missing critical bugs and quality issues."
)
pdf_test_bad.ln(10)
pdf_test_bad.set_font("Arial", 'B', 14)
pdf_test_bad.cell(0, 10, "Skills", ln=True)
pdf_test_bad.set_font("Arial", '', 12)
pdf_test_bad.multi_cell(0, 10, "Basic computer usage, limited testing knowledge")
pdf_test_bad.ln(10)
pdf_test_bad.set_font("Arial", 'B', 14)
pdf_test_bad.cell(0, 10, "Experience", ln=True)
pdf_test_bad.set_font("Arial", '', 12)
pdf_test_bad.multi_cell(0, 10,
    "Worked in non-technical roles with no involvement in software testing or quality assurance."
)
pdf_test_bad.output("sample_resume_testing_bad.pdf")

# ------------- Blockchain Category: Good Match -------------
pdf_blockchain_good = FPDF()
pdf_blockchain_good.add_page()
pdf_blockchain_good.set_font("Arial", 'B', 16)
pdf_blockchain_good.cell(0, 10, "Blockchain Developer Resume - Good Match", ln=True, align="C")
pdf_blockchain_good.ln(10)
pdf_blockchain_good.set_font("Arial", '', 12)
pdf_blockchain_good.cell(0, 10, "Name: Alice Crypto", ln=True)
pdf_blockchain_good.cell(0, 10, "Email: alice.crypto@example.com", ln=True)
pdf_blockchain_good.cell(0, 10, "Phone: 555-222-3333", ln=True)
pdf_blockchain_good.ln(10)
pdf_blockchain_good.set_font("Arial", 'B', 14)
pdf_blockchain_good.cell(0, 10, "Summary", ln=True)
pdf_blockchain_good.set_font("Arial", '', 12)
pdf_blockchain_good.multi_cell(0, 10,
    "Skilled Blockchain Developer with extensive experience in decentralized application development and smart contract programming. "
    "Expert in Ethereum and Hyperledger Fabric, with a strong understanding of cryptography and blockchain protocols."
)
pdf_blockchain_good.ln(10)
pdf_blockchain_good.set_font("Arial", 'B', 14)
pdf_blockchain_good.cell(0, 10, "Skills", ln=True)
pdf_blockchain_good.set_font("Arial", '', 12)
pdf_blockchain_good.multi_cell(0, 10, "Solidity, Ethereum, Hyperledger Fabric, Smart Contracts, Web3.js, Truffle")
pdf_blockchain_good.ln(10)
pdf_blockchain_good.set_font("Arial", 'B', 14)
pdf_blockchain_good.cell(0, 10, "Experience", ln=True)
pdf_blockchain_good.set_font("Arial", '', 12)
pdf_blockchain_good.multi_cell(0, 10,
    "Blockchain Developer at ChainTech (2019-2023): Designed and deployed smart contracts, optimized blockchain protocols, "
    "and built secure decentralized applications."
)
pdf_blockchain_good.output("sample_resume_blockchain_good.pdf")

# ------------- Blockchain Category: Bad Match -------------
pdf_blockchain_bad = FPDF()
pdf_blockchain_bad.add_page()
pdf_blockchain_bad.set_font("Arial", 'B', 16)
pdf_blockchain_bad.cell(0, 10, "Blockchain Developer Resume - Bad Match", ln=True, align="C")
pdf_blockchain_bad.ln(10)
pdf_blockchain_bad.set_font("Arial", '', 12)
pdf_blockchain_bad.cell(0, 10, "Name: Bob NoCrypto", ln=True)
pdf_blockchain_bad.cell(0, 10, "Email: bob.nocrypto@example.com", ln=True)
pdf_blockchain_bad.cell(0, 10, "Phone: 555-444-5555", ln=True)
pdf_blockchain_bad.ln(10)
pdf_blockchain_bad.set_font("Arial", 'B', 14)
pdf_blockchain_bad.cell(0, 10, "Summary", ln=True)
pdf_blockchain_bad.set_font("Arial", '', 12)
pdf_blockchain_bad.multi_cell(0, 10,
    "Lacks practical experience in blockchain technology and decentralized systems. Has minimal understanding of smart contracts "
    "and no proven track record in blockchain development."
)
pdf_blockchain_bad.ln(10)
pdf_blockchain_bad.set_font("Arial", 'B', 14)
pdf_blockchain_bad.cell(0, 10, "Skills", ln=True)
pdf_blockchain_bad.set_font("Arial", '', 12)
pdf_blockchain_bad.multi_cell(0, 10, "Basic computer skills, no blockchain experience")
pdf_blockchain_bad.ln(10)
pdf_blockchain_bad.set_font("Arial", 'B', 14)
pdf_blockchain_bad.cell(0, 10, "Experience", ln=True)
pdf_blockchain_bad.set_font("Arial", '', 12)
pdf_blockchain_bad.multi_cell(0, 10,
    "Worked in traditional IT roles without any exposure to blockchain or decentralized application development."
)
pdf_blockchain_bad.output("sample_resume_blockchain_bad.pdf")

# ------------- Database Administrator Category: Good Match -------------
pdf_db_good = FPDF()
pdf_db_good.add_page()
pdf_db_good.set_font("Arial", 'B', 16)
pdf_db_good.cell(0, 10, "Database Administrator Resume - Good Match", ln=True, align="C")
pdf_db_good.ln(10)
pdf_db_good.set_font("Arial", '', 12)
pdf_db_good.cell(0, 10, "Name: Clara Data", ln=True)
pdf_db_good.cell(0, 10, "Email: clara.data@example.com", ln=True)
pdf_db_good.cell(0, 10, "Phone: 555-666-7777", ln=True)
pdf_db_good.ln(10)
pdf_db_good.set_font("Arial", 'B', 14)
pdf_db_good.cell(0, 10, "Summary", ln=True)
pdf_db_good.set_font("Arial", '', 12)
pdf_db_good.multi_cell(0, 10,
    "Experienced Database Administrator with expertise in managing SQL and NoSQL databases. Proficient in performance tuning, "
    "backup & recovery, and ensuring data security. Successfully maintained high uptime and optimized database operations."
)
pdf_db_good.ln(10)
pdf_db_good.set_font("Arial", 'B', 14)
pdf_db_good.cell(0, 10, "Skills", ln=True)
pdf_db_good.set_font("Arial", '', 12)
pdf_db_good.multi_cell(0, 10, "SQL, NoSQL, Oracle, PostgreSQL, MySQL, Performance Tuning, Backup & Recovery")
pdf_db_good.ln(10)
pdf_db_good.set_font("Arial", 'B', 14)
pdf_db_good.cell(0, 10, "Experience", ln=True)
pdf_db_good.set_font("Arial", '', 12)
pdf_db_good.multi_cell(0, 10,
    "Database Administrator at DataSystems (2017-2023): Managed enterprise-level databases, implemented performance optimizations, "
    "and ensured data integrity and security."
)
pdf_db_good.output("sample_resume_db_good.pdf")

# ------------- Database Administrator Category: Bad Match -------------
pdf_db_bad = FPDF()
pdf_db_bad.add_page()
pdf_db_bad.set_font("Arial", 'B', 16)
pdf_db_bad.cell(0, 10, "Database Administrator Resume - Bad Match", ln=True, align="C")
pdf_db_bad.ln(10)
pdf_db_bad.set_font("Arial", '', 12)
pdf_db_bad.cell(0, 10, "Name: Dave Incompetent", ln=True)
pdf_db_bad.cell(0, 10, "Email: dave.incompetent@example.com", ln=True)
pdf_db_bad.cell(0, 10, "Phone: 555-888-9999", ln=True)
pdf_db_bad.ln(10)
pdf_db_bad.set_font("Arial", 'B', 14)
pdf_db_bad.cell(0, 10, "Summary", ln=True)
pdf_db_bad.set_font("Arial", '', 12)
pdf_db_bad.multi_cell(0, 10,
    "Limited experience in database administration. Lacks essential knowledge of SQL/NoSQL databases, performance tuning, and data security."
)
pdf_db_bad.ln(10)
pdf_db_bad.set_font("Arial", 'B', 14)
pdf_db_bad.cell(0, 10, "Skills", ln=True)
pdf_db_bad.set_font("Arial", '', 12)
pdf_db_bad.multi_cell(0, 10, "Basic computer skills, no database expertise")
pdf_db_bad.ln(10)
pdf_db_bad.set_font("Arial", 'B', 14)
pdf_db_bad.cell(0, 10, "Experience", ln=True)
pdf_db_bad.set_font("Arial", '', 12)
pdf_db_bad.multi_cell(0, 10,
    "Worked in non-technical roles with no direct involvement in database management or administration."
)
pdf_db_bad.output("sample_resume_db_bad.pdf")

print("Sample resume PDFs generated:")
print(" - sample_resume_testing_good.pdf")
print(" - sample_resume_testing_bad.pdf")
print(" - sample_resume_blockchain_good.pdf")
print(" - sample_resume_blockchain_bad.pdf")
print(" - sample_resume_db_good.pdf")
print(" - sample_resume_db_bad.pdf")

print("Sample resume PDFs generated:")
print(" - sample_resume_candidate1.pdf")
print(" - sample_resume_candidate2.pdf")