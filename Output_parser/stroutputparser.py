from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model = "openai/gpt-oss-120b")

prompt = PromptTemplate.from_template(
    "explain {topic} in simple terms"
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({
    "topic" : "machine learning"
})

#print(result)
print(type(result))