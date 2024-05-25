Filename: message_filter.py

# Import necessary libraries
import re

# Define the message filter class
class MessageFilter:
    def __init__(self, banned_words):
        self.banned_words = banned_words

    def filter_message(self, message):
        for word in self.banned_words:
            if re.search(r"\b" + re.escape(word) + r"\b", message, re.IGNORECASE):
                return True
        return False

    def add_banned_word(self, word):
        self.banned_words.append(word)

    def remove_banned_word(self, word):
        if word in self.banned_words:
            self.banned_words.remove(word)

    def get_banned_words(self):
        return self.banned_words

# Sample test
if __name__ == "__main__":
    banned_words = ["bad", "rude", "offensive"]
    filter_obj = MessageFilter(banned_words)
    test_message = "This is a bad message."
    if filter_obj.filter_message(test_message):
        print("Message contains banned words.")
    else:
        print("Message is clean.")