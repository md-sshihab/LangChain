from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")


class ModelEvaluation(BaseModel):

    model_name: str = Field(
        description="name of the machine learning model"
    )

    accuracy: float = Field(
        gt=0,
        lt=1,
        description="accuracy of the machine learning model greater than 0 and less than 1"
    )

    dataset: str = Field(
        description="name of the dataset used for evaluation"
    )


parser = PydanticOutputParser(
    pydantic_object=ModelEvaluation
)


template = PromptTemplate(
    template="""
    Generate the name, accuracy, and dataset for a functional
    model trained for {task}.

    {format_instructions}
    """,
    input_variables=["task"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)


chain = template | model | parser


result = chain.invoke({
    "task": "image_classification"
})


print(type(result))
print(result)