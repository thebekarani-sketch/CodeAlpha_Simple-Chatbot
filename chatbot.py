def chatbot():
    while True:
        user_input = input("You: ").lower()
        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "what is your name":
            print("Bot: My name is ChatBot.")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I'm not sure how to respond to that.")

chatbot()