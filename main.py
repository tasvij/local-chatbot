from interface import ChatInterface

def main():
    # Initialize the chatbot with a better model
    chatbot = ChatInterface(
        model_name="microsoft/DialoGPT-medium",  # Better quality responses
        memory_window=3  # Keep last 3 exchanges (6 messages total)
    )
    
    # Start the chat
    chatbot.start_chat()

if __name__ == "__main__":
    main()