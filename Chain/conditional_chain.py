from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

# Prompt
prompt = PromptTemplate(
    template="Give a short feedback for a student who got {marks} marks.",
    input_variables=["marks"]
)

parser = StrOutputParser()

# Chain
chain = prompt | model | parser

# Conditional branches
conditional_chain = RunnableBranch(
    (
        lambda x: int(x["marks"]) >= 80,
        chain
    ),
    (
        lambda x: int(x["marks"]) >= 50,
        chain
    ),
    RunnableLambda(lambda x: "The student needs improvement.")
)

# Run
result = conditional_chain.invoke({"marks": 85})

print(result)