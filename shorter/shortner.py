import string
import random


class Shortner:
    token_size = 5

    def __init__(self, token_size=None):
        self.token_size = token_size if token_size != None else 5 # defaults sets token size to 5 if no token size is passed

    def issue_token(self):
        letters = string.ascii_letters  # random string ok ascii characters
        # returns a random string of characters from letters
        return ''.join(random.choice(letters) for i in range(self.token_size))

