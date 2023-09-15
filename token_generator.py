import datetime
import hashlib


class TokenGenerator:

    def __init__(self):
        self.token = None
        self.date_string = None

    def get_date_string(self):
        # Get the current date and time
        self.date_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return self.date_string

    def generate_token_by_date(self, date):
        # Hash the date string to create a token
        self.token = hashlib.sha256(date.encode()).hexdigest()

        return self.token

    def get_token(self):
        # Get the date string and generate a token
        date = self.get_date_string()
        token = self.generate_token_by_date(date)

        return token


# Test the token generator
# print(TokenGenerator().generate_token_by_date("2023-09-15 00:00:00"))
