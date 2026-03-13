# Scenario-Based Assessment
# Case Study: AI Assistant for a University Helpdesk

# A large university receives thousands of student queries daily related to admissions, fees, hostel facilities, course
#  schedules, and exam results.

# Currently, these queries are answered manually by staff, causing:

# Slow response time

# High operational cost

# Inconsistent responses

# The university plans to develop an AI-powered chatbot using Generative AI and Large Language Models (LLMs) to
#  automatically respond to student questions.

# You are part of the AI consulting team tasked with designing the solution.

# ==========================================
# UNIVERSITY AI HELPDESK CHATBOT
# Demonstrates:
# Generative AI
# Large Language Models (LLMs)
# Tokenization
# Transformer Inference
# Prompt Engineering
# ==========================================

# Install required libraries first
# pip install transformers torch

# STEP 3: Define University Knowledge Base
# # ------------------------------------------
# knowledge_base = """
# University Helpdesk Information

# Hostel Admission Requirements:
# - Admission confirmation letter
# - Government ID proof
# - Two passport size photographs

# Course Registration:
# - Registration happens online through the university portal
# - Students must register before the semester deadline

# Fee Payment:
# - Fees can be paid through the student dashboard
# - Online payment methods include debit card, credit card, and net banking

# Examination Schedule:
# - Semester exams usually start in December and May

# Library Access:
# - Students must carry their university ID card
# """


from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

# Load environment variables (MISTRAL_API_KEY from .env)
load_dotenv()

# Initialize Mistral model
model = init_chat_model("mistral-medium-latest")

# University Knowledge Base
knowledge_base = """
University Helpdesk Information

Hostel Admission Requirements:
- Admission confirmation letter
- Government ID proof
- Two passport size photographs

Course Registration:
- Registration happens online through the university portal
- Students must register before the semester deadline

Fee Payment:
- Fees can be paid through the student dashboard
- Online payment methods include debit card, credit card, and net banking

Examination Schedule:
- Semester exams usually start in December and May

Library Access:
- Students must carry their university ID card
"""

print("🎓 University Helpdesk Chatbot")
print("Type 'exit' to stop the chatbot\n")

while True:

    question = input("Student: ")
    print("=="*100)
    if question.lower() == "exit":
        print("Chatbot: Goodbye! 👋")
        break

    prompt = f"""
You are a helpful university helpdesk assistant.

Use the information below to answer the student's question.

{knowledge_base}

Student Question: {question}

Answer:
"""
    res = model.invoke(prompt)

    print("\nChatbot:", res.content)
    print()