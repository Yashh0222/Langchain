from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)
#temperature: 1} if we set it to "0" then content remain same for every search 
            # 2} if we set it to any other then answer change on every search 
#token used to set tokens
result = model.invoke("write 5 line poem on cricket")

print(result.content) #content gives main answer from all output