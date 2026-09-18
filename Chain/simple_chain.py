from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()

prompt = PromptTemplate(
    template="""
    You are an AI tutor .
    Explain the following topic to the student in simple way
    topic {topic}
    """,
    input_variables=['topic']
    
)

model = ChatGroq(model="openai/gpt-oss-120b")

parser = StrOutputParser()

prompt_value = prompt.invoke({"topic":"machine learning"})

model_output = model.invoke(prompt_value)

final_output = parser.invoke(model_output)

print(final_output)