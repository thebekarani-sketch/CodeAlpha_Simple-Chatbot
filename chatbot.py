def chatbot():
    while True:
        user_input = input("You: ").lower()
        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I'm not sure how to respond to that.")

chatbot()