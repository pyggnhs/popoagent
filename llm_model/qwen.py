from langchain_openai import ChatOpenAI
llm_model = ChatOpenAI(
    model="qwen-plus",
    temperature=0,
)