from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    max_new_tokens=100,
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of Bangladesh?")

print(result.content)