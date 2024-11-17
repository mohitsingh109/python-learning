# 1 ... 10
# [1, 4, 9, 6, 25, ... 100]

# squares = []
# for x in range(1, 11):
#     value = x * x # x ^ 2
#     squares.append(value)

squares = [x ** 2 for x in range(1, 11)]
print(squares)

actual_name = ["Mohit", "Karan", "Arjun"]
names = ["Hello " + name + " !" for name in actual_name]
print(names)


