from langchain_community.document_loaders import PyPDFLoader

#used to load pdf and after loading pypdf loader converts it into list where each page is seperated 
loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[3].page_content)
print(docs[3].metadata)