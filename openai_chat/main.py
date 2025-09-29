from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, Tool
from langchain_community.utilities import SerpAPIWrapper

load_dotenv()

app = FastAPI()

# ==================
# Environment Variables
# ==================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# ==================
# Chat Model + Memory
# ==================
llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=OPENAI_API_KEY)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# ==================
# Tools
# ==================
search = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful for answering finance questions from the internet"
    )
]

# ==================
# Agent Initialization
# ==================
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="conversational-react-description",
    memory=memory,
    verbose=True
)

# ==================
# Finance Filtering
# ==================
finance_keywords = ["finance", "investment", "stock", "bank", "loan", "mortgage", "money"]

def is_finance_question(question: str) -> bool:
    return any(word in question.lower() for word in finance_keywords)

# ==================
# API Endpoint
# ==================
@app.post("/chat")
async def chat_endpoint(request: Request):
    body = await request.json()
    user_message = body.get("message", "").strip()

    if not is_finance_question(user_message):
        return JSONResponse({"response": "I am a finance assistant and can only answer finance-related queries."})

    # Pass finance question to LangChain agent
    response = agent.run(user_message)
    return JSONResponse({"response": response})

# ==================
# UI Endpoint
# ==================
@app.get("/", response_class=HTMLResponse)
async def chat_ui():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI Finance Agent Chat</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background-color: #f8f9fa; }
            #chat-box {
                border: 1px solid #ced4da;
                border-radius: 8px;
                padding: 15px;
                height: 400px;
                overflow-y: auto;
                background-color: #ffffff;
            }
            .user { color: #0d6efd; margin: 5px 0; }
            .bot { color: #198754; margin: 5px 0; }
            .chat-input-group { position: sticky; bottom: 0; background: #f8f9fa; padding-top: 10px; }
        </style>
    </head>
    <body>
        <div class="container py-4">
            <h2 class="text-center mb-4">AI Finance Agent Chat</h2>
            <div id="chat-box" class="mb-3 shadow-sm"></div>
            <div class="input-group chat-input-group">
                <input id="message" type="text" class="form-control" placeholder="Type a finance question...">
                <button class="btn btn-primary" onclick="sendMessage()">Send</button>
            </div>
        </div>
        <script>
            async function sendMessage() {
                const msg = document.getElementById("message").value.trim();
                if (!msg) return;

                let chatBox = document.getElementById("chat-box");
                chatBox.innerHTML += `<div class='user'><b>You:</b> ${msg}</div>`;

                try {
                    const res = await fetch("/chat", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ message: msg })
                    });
                    const data = await res.json();
                    chatBox.innerHTML += `<div class='bot'><b>AI:</b> ${data.response}</div>`;
                } catch (err) {
                    chatBox.innerHTML += `<div class='bot text-danger'><b>AI:</b> Error connecting to server</div>`;
                }

                chatBox.scrollTop = chatBox.scrollHeight;
                document.getElementById("message").value = "";
            }

            document.getElementById("message").addEventListener("keypress", function(e) {
                if (e.key === "Enter") sendMessage();
            });
        </script>
    </body>
    </html>
    """
