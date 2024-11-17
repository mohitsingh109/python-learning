# try, Exception, Finally

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Yar can't divide by 0")
finally:
    print("End of error handling")

# Raise exception
age = int(input("Enter your age: "))
if age < 18:
    raise ValueError("Age must be 18 or above")
else:
    print("welcome !!!")


class CustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise CustomError("This is a custom exception")
except CustomError as e:
    print("Caught an exception", e.message)