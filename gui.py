import tkinter as tk
from tkinter import scrolledtext
from chatbot import get_response

def send_message():
    user_input = entry.get()
    if user_input.lower() == 'exit':
        root.quit()
    
    context = chat_display.get("1.0", tk.END)
    result = get_response(context, user_input)

    chat_display.configure(state='normal')
    chat_display.insert(tk.END, f"You: {user_input}\nAI: {result}\n")
    chat_display.configure(state='disabled')
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("AI ChatBot")

chat_display = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD)
chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, width=80)
entry.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.X, expand=True)
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10, side=tk.RIGHT)

def run_gui():
    root.mainloop()
