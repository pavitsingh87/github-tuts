from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, Tool
from langchain_community.utilities import SerpAPIWrapper
from config import OPENAI_API_KEY, SERPAPI_API_KEY, FINANCE_KEYWORDS
from models import user_memories

# Chat Model
llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=OPENAI_API_KEY)

# Tools
search = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful for answering finance questions from the internet"
    )
]

def get_user_agent(user_id: str):
    if user_id not in user_memories:
        user_memories[user_id] = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent="conversational-react-description",
        memory=user_memories[user_id],
        verbose=True
    )

def is_finance_question(question: str) -> bool:
    return any(word in question.lower() for word in FINANCE_KEYWORDS)