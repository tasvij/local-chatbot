class ConversationMemory:
    def __init__(self, window_size=4):
        """
        Initialize conversation memory with a sliding window.
        window_size: number of exchanges to keep (each exchange = user + bot)
        """
        self.window_size = window_size
        self.history = []
    
    def add_exchange(self, user_message, bot_message):
        """Add a new user-bot exchange to the history"""
        self.history.append({"user": user_message, "bot": bot_message})
        
        # Apply sliding window - remove oldest exchanges if we exceed the window size
        while len(self.history) > self.window_size:
            self.history.pop(0)
    
    def get_recent_history(self, num_exchanges=None):
        """
        Get recent conversation history.
        num_exchanges: if specified, return only the last N exchanges
        """
        if num_exchanges is None:
            return self.history.copy()
        else:
            return self.history[-num_exchanges:].copy()
    
    def clear_history(self):
        """Clear the conversation history"""
        self.history = []
    
    def get_formatted_history(self, num_exchanges=None):
        """
        Get formatted history for model input
        """
        recent_history = self.get_recent_history(num_exchanges)
        return recent_history
    
    def __len__(self):
        return len(self.history)
