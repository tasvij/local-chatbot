from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

class ModelLoader:
    def __init__(self, model_name="microsoft/DialoGPT-medium"):  # Changed to medium for better quality
        self.model_name = model_name
        self.tokenizer = None
        self.model = None
        self.pipeline = None
        self.is_loaded = False
        
    def load_model(self):
        """Load the model and tokenizer from Hugging Face"""
        try:
            print(f"Loading model {self.model_name}...")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
            
            # Create text generation pipeline with better settings
            self.pipeline = pipeline(
                "text-generation",
                model=self.model,
                tokenizer=self.tokenizer,
                pad_token_id=self.tokenizer.eos_token_id,
                truncation=True,  # Fixes truncation warning
                max_new_tokens=100,  # Better response length
                temperature=0.9,  # More creative but coherent
                do_sample=True,
                top_p=0.9,  # Better quality responses
                repetition_penalty=1.1  # Reduce repetition
            )
            
            self.is_loaded = True
            print("Model loaded successfully!")
            return True
            
        except Exception as e:
            print(f"Error loading model: {e}")
            return False
    
    def generate_response(self, input_text, history=None):
        """Generate a response using the loaded model"""
        if not self.is_loaded:
            return "Error: Model not loaded."
        
        try:
            # Prepare the input text with history if available
            if history:
                # Format the conversation history
                formatted_history = " ".join(
                    [f"User: {turn['user']} Bot: {turn['bot']}" for turn in history]
                )
                full_input = f"{formatted_history} User: {input_text} Bot:"
            else:
                full_input = f"User: {input_text} Bot:"
            
            # Generate response
            outputs = self.pipeline(
                full_input,
                num_return_sequences=1,
                pad_token_id=self.tokenizer.eos_token_id
            )
            
            # Extract the generated text
            generated_text = outputs[0]['generated_text']
            
            # Extract only the bot's response (the part after the last "Bot:")
            response = generated_text.split("Bot:")[-1].strip()
            
            # Clean up the response (remove any remaining "User:" parts)
            if "User:" in response:
                response = response.split("User:")[0].strip()
                
            return response
            
        except Exception as e:
            return f"Error generating response: {e}"