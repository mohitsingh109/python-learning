# Function
def greet(name):
    return f"Hello {name}!. How are you?"


def multiple_return_date_type(condition):
    if condition == 0:
        return "Hello"
    elif condition == 1:
        return 100
    elif condition == 2:
        return ["Mohit", "Karan"]


def multiple_return_multiple_values():
    return "Mohit", 10, ["A", "B"]


print(greet("Mohit"))


name, age, task = multiple_return_multiple_values()
print(task)
