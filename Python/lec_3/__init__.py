def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y


user_input = input("Write your calculate:")
operator = None
ind = 0

for char in user_input:
    if char in ('+', '-', '*', '/'):
        operator = char
        break
    ind += 1

a, b = user_input.split(operator)
a = float(a)
b = float(b)

if operator == '+':
    print(add(a, b))
elif operator == '-':
    print(subtract(a, b))
elif operator == '*':
    print(multiply(a, b))
elif operator == '/':
    print(divide(a, b))
