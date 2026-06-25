def welcome():
    print("\n" + "=" * 50)
    print("WELCOME TO SIMPLE CHATBOT")
    print("=" * 50)
    print("I can answer a few basic questions.")
    print("Try saying:")
    print(" * hello")
    print(" * how are you")
    print(" * what is your name")
    print(" * what can you do")
    print(" * thank you")
    print(" * bye")
    print("-" * 50)
    print("Type 'bye' anytime to exit.")
    print("=" * 50 + "\n")
def get_response(message):
    if message == "hello":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"  
    elif message == "what is your name":
        return "My name is ChatBot."
    elif message == "what can you do":
        return "I can chat with you and answer simple questions."
    elif message == "thank you":
        return "My pleasure!"
    elif message == "bye":
        return "Goodbye!"
    else:
        return "I'm not sure how to respond to that."
 
def chatbot():
    welcome()
    while True:
        user_input = input("You: ").lower()
        response = get_response(user_input)
        print("Bot: ",response)
        if user_input == "bye":
            break

chatbot()