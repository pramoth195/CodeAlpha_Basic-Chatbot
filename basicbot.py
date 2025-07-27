def get_response(user_input):
    user_input = user_input.lower().strip()
    
    if user_input == "hello":
        return "Hi there!"
    elif user_input == "hi":
        return "Hello!"
    elif user_input == "how are you":
        return "I'm good!"
    elif user_input == "what's up":
        return "Not much!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Hmm, interesting..."

def chatbot():
    print("\nWelcome to the Simple Python Chatbot!")
    print("Type 'bye' to exit.\n")
    print("Hi there! I'm a simple Python chatbot. You can ask me anything!")
    print("Try saying: hello, how are you, or bye\n")

    while True:
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
            
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        
        if user_input.lower() == "bye":
            print("The chatbot has logged off. Run again to chat!")
            break

if __name__ == "__main__":
    chatbot()
