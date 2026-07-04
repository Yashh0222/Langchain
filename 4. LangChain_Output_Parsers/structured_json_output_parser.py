from langchain_groq import ChatGroq
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
# from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")
# THis is json_output_parser which gives result in jsson format 
#  and here we can decide schema of output parser gives on its own  

schema = [
    ResponseSchema(name='fact_1', description='fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schema(schema)

template = PromptTemplate(
    template='Give me 3 facts on {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction' : parser.get_format_instruction()}
)

chain = template | model | parser

result = chain.invoke({'topic': 'black hole'})

print(result)