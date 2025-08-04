import tkinter as tk

# Load responses from file
def load_responses():
    responses = {}
    with open("responses.txt", "r") as file:
        for line in file:
            if ":" in line:
                key, value = line.strip().split(":", 1)
                responses[key.lower()] = value
    return responses

# Get response from loaded rules
def get_response(user_input, responses):
    user_input = user_input.lower()
    for question in responses:
        if question in user_input:
            return responses[question]
    return "I'm not sure how to respond to that."

# GUI setup
def send():
    user_input = entry.get()
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    response = get_response(user_input, chatbot_responses)
    chat_log.insert(tk.END, "Bot: " + response + "\n")
    entry.delete(0, tk.END)

# GUI window
root = tk.Tk()
root.title("Rule-Based Chatbot")

chat_log = tk.Text(root, height=20, width=50)
chat_log.pack()

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=(10, 0))

send_button = tk.Button(root, text="Send", command=send)
send_button.pack(side=tk.LEFT)

chatbot_responses = load_responses()

root.mainloop()

