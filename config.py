import json
import os

class Config:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.default_config = {
            "model_name": "microsoft/DialoGPT-medium",
            "memory_window": 4,
            "max_tokens": 100,
            "temperature": 0.9,
            "enable_logging": True,
            "log_file": "conversations.json"
        }
        self.config = self.load_config()
        
    def load_config(self):
        """Load configuration from file or use defaults"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as f:
                    loaded_config = json.load(f)
                    # Merge with defaults (loaded config overrides defaults)
                    return {**self.default_config, **loaded_config}
            except Exception as e:
                print(f"Error loading config: {e}. Using defaults.")
                return self.default_config
        return self.default_config
        
    def save_config(self):
        """Save current configuration to file"""
        try:
            with open(self.config_file, "w") as f:
                json.dump(self.config, f, indent=2)
            print(f"Configuration saved to {self.config_file}")
        except Exception as e:
            print(f"Error saving config: {e}")
            
    def get(self, key, default=None):
        """Get a configuration value"""
        return self.config.get(key, default)