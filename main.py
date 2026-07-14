import my_utils
import calculator
import random  
import Patterns 
import datetime as dt

print(my_utils.greet("World"))
print("Sum:", my_utils.add(5, 3))
print("Product:", my_utils.multiply(5, 3))      
print("Triangle:")
my_utils.print_triangle(5)

calc = calculator
print("Addition:", calc.add(10, 5))
print("Multiplication:", calc.multiply(10, 5))  
print("Subtraction:", calc.substraction(10, 5))
print("Division:", calc.divide(10, 5))
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)
print("password of 8 Character:", random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
print("Print triangle")

patterns = Patterns

patterns.print_rectangle(5, 8)  
print(f"Current datetime: {dt.datetime.now()}")