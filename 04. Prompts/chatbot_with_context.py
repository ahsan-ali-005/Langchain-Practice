from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

chat_history = []

# now keeps context but can't understand which message is from user and which from AI itself
# so use Messages for this..

while True:
    user = input("You: ")
    chat_history.append(user)
    if user == "exit":
        break
    response = model.invoke(chat_history)
    chat_history.append(response.content[0]["text"].strip())
    print(f"AI: {response.content[0]["text"].strip()}")