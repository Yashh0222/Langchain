from langchain_groq import ChatGroq
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")
# THis is json_output_parser which gives result in jsson format 
#  but we cant decide schema of output parser gives on its own  
parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me name, age and city of frictional person \n {format_instruction}',
    input_variable=[],
    partial_variables={'format_instruction': parser.get_format_instructions}
)

chain = template | model | parser

result = chain.invoke({})

print(result)
