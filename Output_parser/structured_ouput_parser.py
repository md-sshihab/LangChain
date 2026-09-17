from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers.structured import(
    StructuredOutputParser,ResponseSchema
)
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

response_schema =[ 
    ResponseSchema(
        name = "fact  1",
        description = "first fact of the topic"
    ),
    ResponseSchema(
        name = "fact  2",
        description = "seccond fact of the topic"
    ),
    ResponseSchema(
        name = "fact  3",
        description = "thied fact of the topic"
    ),
    ResponseSchema(
        name = "fact  4",
        description = "forth fact of the topic"
    ),
    ResponseSchema(
        name = "fact  5",
        description = "fifth fact of the topic"
    ),
]

parser = StructuredOutputParser.from_response_schemas(
    response_schema
)

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
#print(result)
print(result['fact  1'])