def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b        

def multiply(a, b):
    return a * b        

def print_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i)
print_triangle(5)      