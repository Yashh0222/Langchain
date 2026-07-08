from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

prompt = PromptTemplate(
    template="write summary on following poem \n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

# used to load text file and extract content and metadata
loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

print(type(docs))  

print(docs[0].page_content)
print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem': docs[0].page_content}))