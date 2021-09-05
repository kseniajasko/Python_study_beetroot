# Create your custom exception named `CustomException`, you can inherit from base Exception class,
# but extend its functionality to log every error message to a file named `logs.txt`.
# Tips: Use __init__ method to extend functionality for saving messages to file

class CustomException(Exception):
    def __init__(self, number, message="Number is not in (5000, 15000) 1 range"):
        self.number = number
        self.message = message
        super().__init__(self.message)

        with open('logs.txt', 'a') as file_object:
            file_object.write(f'{self.message}:{self.number}\r\n')

try:
    number1 = int(input("Enter number: "))
    if not 5000 < number1 < 15000:
        raise CustomException(number1)
except CustomException:
    print("Error found")


