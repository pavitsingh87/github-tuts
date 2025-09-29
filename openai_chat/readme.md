
# OpenAI Finance Chat Agent

A **FastAPI-based AI chatbot** that only answers finance-related queries, powered by **LangChain** and **OpenAI GPT-4o-mini**. Users can interact with the bot through a simple web interface, and the bot integrates **SerpAPI** for finance-related web search results.

---

## Features

- AI assistant specialized in **finance topics**: investments, banking, loans, mortgages, stock markets.
- **Web interface** for chat using HTML, Bootstrap, and JavaScript.
- **Memory** support: remembers conversation history using LangChain `ConversationBufferMemory`.
- **Tool integration**: SerpAPI to fetch relevant online data for finance questions.
- **Environment-based API keys**: `.env` file for sensitive credentials.
- Mobile-friendly and responsive UI.

---

## Demo

Open the app in your browser:

```

https://0f46d6695d26.ngrok-free.app/

````

You can also expose it via **ngrok**:

```bash
ngrok http 8000
````

---

## Installation

1. **Clone the repository**:

```bash
git clone <your-gitlab-repo-url>
cd openai_chat
```

2. **Create a virtual environment**:

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file**:

```env
OPENAI_API_KEY=your_openai_api_key
SERPAPI_API_KEY=your_serpapi_api_key
```

---

## Usage

Run the FastAPI app with Uvicorn:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

* Open your browser at `http://localhost:8000`
* Type finance-related questions in the chat box.
* Bot will **only answer finance-related queries**; other questions will get a polite rejection:
  *"I am a finance assistant and can only answer finance-related queries."*

---

## Project Structure

```
openai_chat/
├── main.py           # FastAPI app + LangChain agent
├── .env              # API keys (not committed to Git)
├── requirements.txt  # Python dependencies
└── README.md
```

---

## Dependencies

* fastapi
* uvicorn
* langchain
* openai
* python-dotenv
* requests
* serpapi

You can install all dependencies at once using:

```bash
pip install -r requirements.txt
```

---

## Notes

* Make sure `.env` is **never pushed** to GitHub (add to `.gitignore`).
* This bot is **finance-specific**; all non-finance queries are politely rejected.
* UI is **mobile-friendly** using Bootstrap.
* You can use **ngrok** to expose your local server publicly for testing.

---

## Example Usage

```text
You: How can I invest in the stock market?
AI: You can start investing by opening a brokerage account and diversifying across ETFs, stocks, and bonds.

You: Who won the last cricket match?
AI: I am a finance assistant and can only answer finance-related queries.
```

---

## License

This project is **MIT licensed**.

```

---

If you want, I can also create a **ready-to-use GitHub repo setup guide**, including `.gitignore`, `requirements.txt`, and this README fully integrated so you can push it immediately.  

Do you want me to do that?
```
