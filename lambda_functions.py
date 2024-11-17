# lambda arguments: expression

# Lambda to add 10 to a number
# def add_10_num(value):
#     return value + 10

add_ten = lambda x: x + 10
print(add_ten(20))

# Lambda to multiply two numbers
multiply = lambda x, y: x * y
print(multiply(10, 20))

# map()
# Syntax: map(function, iterable)
nums = [1, 2, 3, 4, 5, 6]
squared = map(lambda x: x ** 2, nums)
print(list(squared))

# filter()
# Syntax: filter(function, iterable)

nums = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, nums)
print(list(even))

# lambda, map, filter
# Square only the even numbers
squared_even = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums))
print(list(squared_even))
