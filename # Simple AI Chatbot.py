# Simple AI Chatbot

print("Hello! I am ChatBot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How are you?")
    elif "How can I help you ?":
    
        print("Bot: I'm just a bot, but I'm doing fine! How about you?")
    elif "your name" in user_input:
        print("Bot: I am ChatBot, your friendly AI.")
    elif "bye" in user_input:
        print("Bot: Goodbye! Have a nice day!")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")