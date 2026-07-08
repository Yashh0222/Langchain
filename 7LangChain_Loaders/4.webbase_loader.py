from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

prompt = PromptTemplate(
    template="Answer the question {question} based on following text \n {text}",
    input_variables=['question', 'text']
)

parser = StrOutputParser()

url = "https://www.flipkart.com/search?q=macbook&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=macbook%7CLaptops&requestId=19dc9afb-9e7b-44c5-aac2-d2b4e044737c&as-backfill=on"

#webbaseloader is used to get data from live url and we can ask questions 
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question':'what is product we are talking about ?', 'text':docs[0].page_content}))