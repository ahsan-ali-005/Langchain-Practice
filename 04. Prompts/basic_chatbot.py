from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

# problem no context can't remember previous conversation

while True:
    user = input("You: ")
    if user == "exit":
        break
    response = model.invoke(user)
    print(f"AI: {response.content[0]["text"].strip()}")