from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict  ,  Annotated , Literal , Optional

load_dotenv()

model = ChatGroq(model = "openai/gpt-oss-120b")

#define the schema

class ResumeAnalysis(TypedDict):
    key_skill : Annotated[list[str], "Extract all important and soft skills from the resume"]
    summary : Annotated[str, "write a brief summary of the  candidate's profile"]
    experience_level : Annotated[Literal["entry_level","mid_level","senior_level"],"classify the candidate's experience level"]
    strengths : Annotated[Optional[list[str]], "list the candidate's major strength"]
    weakness : Annotated[Optional[list[str]], "list the candida's weakness or areas for improvement"]
    candidate_name : Annotated[str , "Extract the name of the candidate from the resume"]
    
    
    
structured_model = model.with_structured_output(ResumeAnalysis)

result = structured_model.invoke(
    """My name is  Mahir Tajuar Akash. I am a Computer Science graduate with two years
    of experience working as a Machine Learning Engineer.

    I have experience with Python, PyTorch, TensorFlow, Scikit-learn,
    FastAPI, Docker, Kubernetes, MLflow, and AWS. I have built machine
    learning pipelines, deployed deep learning models, and developed
    REST APIs for AI applications.

    I also have experience working with LangChain and Retrieval-Augmented
    Generation (RAG) systems.

    My main strength is my ability to build complete machine learning
    systems from data preprocessing to deployment. However, I have limited
    experience managing large engineering teams and need to improve my
    system design skills.

    Education:
    BSc in Computer Science and Engineering.
    """
)

print(result)