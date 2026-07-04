from langchain_groq import ChatGroq
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

prompt1 = PromptTemplate(
    template='give me a report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='give me 5 pointer summary for following text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser 

result = chain.invoke({'topic':'unemployment in india'})

print(result)