from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()

prompt1 = PromptTemplate(
    template="""
    Evaluate the following student's answer.

    Question: {Question}
    Student's Answer: {answer}

    Provide a detailed evaluation on:
    - Correctness
    - Strength
    - Weakness
    - Suggestions for improvement
    """,
    input_variables=["Question", "answer"]
)

prompt2 = PromptTemplate(
    template="""
    Convert the detailed evaluation into concise 5-point feedback.

    {evaluation}
    """,
    input_variables=["evaluation"]
)

model = ChatGroq(model="openai/gpt-oss-120b")

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({
    "Question": "What is Machine learning",
    "answer": """
    Machine learning is a subset of artificial intelligence
    where computers learn patterns from data and make predictions
    without being explicitly programmed for every step.
    """
})

print(result)

chain.get_graph().print_ascii()