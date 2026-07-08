from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

#used to load multiple pdf at once 
# it takes time to load there is alternative lazyload whic loades what doc we need for now 
loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls = PyPDFLoader
)

docs = loader.load()

print(docs[325].page_content)
print(docs[325].metadata)