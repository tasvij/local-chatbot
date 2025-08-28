import json
from datetime import datetime

class ConversationLogger:
    def __init__(self, log_file="conversations.json"):
        self.log_file = log_file
        
    def log_conversation(self, user_input, bot_response, history=None):
        """Log a conversation exchange to file"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "user_input": user_input,
            "bot_response": bot_response,
            "history": history or []
        }
        
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
        except Exception as e:
            print(f"Logging error: {e}")
            
    def read_logs(self):
        """Read all conversation logs"""
        try:
            if os.path.exists(self.log_file):
                with open(self.log_file, "r", encoding="utf-8") as f:
                    return [json.loads(line) for line in f.readlines()]
            return []
        except Exception as e:
            print(f"Error reading logs: {e}")
            return []