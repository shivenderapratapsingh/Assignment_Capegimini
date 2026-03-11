#  Scenario: AI‑Powered Email Assistant
# You’re building an email drafting assistant for a corporate team.
# - When a user starts typing:
# “Artificial Intelligence will…”
# - The assistant uses GPT‑2 to auto‑complete the sentence with a coherent continuation.
# - Example output:
# “Artificial Intelligence will transform the way businesses interact with customers,
# enabling faster decisions and personalized experiences.”
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

model = init_chat_model("mistral-medium-latest")

res = model.invoke("What is Artificial Intlligence")

print(res.content)