from model_loader import ModelLoader
from chat_memory import ConversationMemory

class ChatInterface:
    def __init__(self, model_name="microsoft/DialoGPT-small", memory_window=4):
        self.model_loader = ModelLoader(model_name)
        self.memory = ConversationMemory(memory_window)
        self.is_running = False
    
    def setup(self):
        """Setup the chatbot by loading the model"""
        print("Setting up chatbot...")
        success = self.model_loader.load_model()
        if not success:
            print("Failed to load model. Exiting.")
            return False
        return True
    
    def start_chat(self):
        """Start the chat loop"""
        if not self.model_loader.is_loaded:
            if not self.setup():
                return
        
        self.is_running = True
        print("\n" + "="*50)
        print("Chatbot is ready! Type your message below.")
        print("Type '/exit' to quit or '/clear' to clear memory")
        print("="*50 + "\n")
        
        while self.is_running:
            try:
                # Get user input
                user_input = input("User: ").strip()
                
                # Check for commands
                if user_input.lower() == "/exit":
                    self.stop_chat()
                    continue
                elif user_input.lower() == "/clear":
                    self.memory.clear_history()
                    print("Bot: Conversation history cleared!")
                    continue
                elif user_input.lower() == "":
                    continue
                
                # Generate response
                history = self.memory.get_formatted_history()
                bot_response = self.model_loader.generate_response(user_input, history)
                
                # Display response
                print(f"Bot: {bot_response}")
                
                # Add to memory
                self.memory.add_exchange(user_input, bot_response)
                
            except KeyboardInterrupt:
                print("\n\nInterrupted by user. Exiting...")
                self.stop_chat()
            except Exception as e:
                print(f"Error: {e}")
                print("Bot: I encountered an error. Please try again.")
    
    def stop_chat(self):
        """Stop the chat loop"""
        self.is_running = False
        print("\nExiting chatbot. Goodbye!")
