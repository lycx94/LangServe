from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
from fastapi import FastAPI
import uvicorn
import os

os.environ['OPENAI_API_KEY'] = "API_KEY"

app = FastAPI(
    title = "LangChain Server",
    version = "1.0",
    description = "API Server"
)

add_routes(
    app,
    ChatOpenAI(),
    path = "/openai"
)


model = ChatOpenAI()
prompt_menu = ChatPromptTemplate.from_template("provide me a menu of {topic}")
prompt_introduction = ChatPromptTemplate.from_template("provide me a short introduction of {topic}")
prompt_review = ChatPromptTemplate.from_template("provide me a review of {topic}")


add_routes(
    app,
    prompt_menu|model,
    path = "/menu"
)

add_routes(
    app,
    prompt_introduction|model,
    path = "/introduction"
)

add_routes(
    app,
    prompt_review|model,
    path = "/review"
)



if __name__ == "__main__":
    uvicorn.run(
        app,
        host = "localhost",
        port = 8000
    )