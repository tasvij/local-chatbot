import unittest
from chat_memory import ConversationMemory

class TestChatbot(unittest.TestCase):
    def test_memory_window(self):
        """Test that memory respects the sliding window size"""
        memory = ConversationMemory(window_size=2)
        memory.add_exchange("Hello", "Hi there!")
        memory.add_exchange("How are you?", "I'm good!")
        memory.add_exchange("What's your name?", "I'm ChatBot")
        
        self.assertEqual(len(memory), 2)  # Should only keep last 2 exchanges
        self.assertEqual(memory.history[0]["user"], "How are you?")
        self.assertEqual(memory.history[1]["user"], "What's your name?")
        
    def test_clear_memory(self):
        """Test that memory can be cleared"""
        memory = ConversationMemory()
        memory.add_exchange("Test", "Response")
        self.assertEqual(len(memory), 1)
        memory.clear_history()
        self.assertEqual(len(memory), 0)
        
    def test_get_recent_history(self):
        """Test getting recent history"""
        memory = ConversationMemory(window_size=3)
        memory.add_exchange("First", "Response 1")
        memory.add_exchange("Second", "Response 2")
        
        recent = memory.get_recent_history(1)
        self.assertEqual(len(recent), 1)
        self.assertEqual(recent[0]["user"], "Second")

if __name__ == "__main__":
    unittest.main()