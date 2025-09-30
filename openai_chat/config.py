import os
from dotenv import load_dotenv

load_dotenv()

# Environment Variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# Finance Keywords
FINANCE_KEYWORDS = ["finance", "investment", "stock", "bank", "loan", "mortgage", "money"]