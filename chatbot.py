def chatbot():
    print("Chatbot: Hello! I'm your assistant. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'exit':
            print("Chatbot: Goodbye! Have a great day.")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just code, but I'm working fine! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I'm a simple chatbot written in Python.")
        elif "help" in user_input:
            print("Chatbot: I can respond to greetings and simple questions. Try saying 'hello' or 'how are you'.")
        else:
            print("Chatbot: I'm not sure how to respond to that.")

chatbot()
