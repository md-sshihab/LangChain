from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

parser = JsonOutputParser()

template = PromptTemplate(
    template="""
    Give me five facts about {topic}.

    {format_instructions}
    """,
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

chain = template | model | parser

result = chain.invoke({
    "topic": "machine learning"
})

print(type(result))
print(result)