# Create a class method named `validate`, which should be called from the `__init__` method
# to validate parameter email, passed to the constructor. The logic inside the `validate`
# method could be to check if the passed email parameter is a valid email string.

import re

class Email:
    def __init__(self, email):
        self.email = self.validate(email)

    def validate(self, email):
        if (re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", email)):
            print(f'This is a valid email address')
            return email
        else:
            print(f"This is not a valid email address")

Email('satur@gmail.com')
Email('satur@gmail.com.ua')
Email('saturmailcom.ua')
Email('satur@gmailcom')