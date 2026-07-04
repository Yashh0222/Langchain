from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Groq model
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=1.5,
    #max_tokens=10
)

# Invoke the model
result = model.invoke("Write a 5-line poem on cricket.")

# Print only the response content
print(result.content)