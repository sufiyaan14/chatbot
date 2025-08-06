import tkinter as tk
from tkinter import scrolledtext

# Simple rule-based response function
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing well! How about you?"
    elif "your name" in user_input:
        return "I'm your friendly Python chatbot!"
    elif "help" in user_input:
        return "Try saying 'hello', 'how are you', or ask me anything."
    elif "bye" in user_input:
        return "Goodbye! Have a great day."
    else:
        return "Sorry, We can do"

# Send message to chat window
def send_message():
    user_input = entry.get()
    chat_window.insert(tk.END, f"You: {user_input}\n")
    response = get_bot_response(user_input)
    chat_window.insert(tk.END, f"Bot: {response}\n\n")
    entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Python GUI Chatbot")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_window.pack(padx=10, pady=10)

entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(padx=10, pady=5)
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(pady=5)

# Start GUI loop
root.mainloop()

