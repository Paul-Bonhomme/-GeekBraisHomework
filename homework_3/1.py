a = int(input("Enter a:"))
b = int(input("Enter b:"))

def func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error!"

print(func(a, b))