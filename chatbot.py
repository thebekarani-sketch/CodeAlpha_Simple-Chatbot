def get_response(message):
    if message == "hello":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"  
    elif message == "what is your name":
        return "My name is ChatBot."
    elif message == "bye":
        return "Goodbye!"
    else:
        return "I'm not sure how to respond to that."
 
 def chatbot():
    while True:
        user_input = input("You: ").lower()
        response = get_response(user_input)
        print("Bot: ",response)
        if user_input == "bye":
            break

chatbot()