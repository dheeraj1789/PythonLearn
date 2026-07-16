def sum_All(*args):
    total=0
    for num in args:
        total+=num
        return total
    
print("sum of all",sum_All(1,2,3,4,5))
print("sum of all",sum_All(10,20,30,40,50))

#you can mix positional and keyword arguments in a function call. However, positional arguments must come before keyword arguments.
def greet_user(greeting,*args):
    for name in args:
        print(f"{greeting} {name}")
print("Greeting users:")
greet_user("Hello","John","Alice","Bob")

#lamda
square = lambda x: x ** 2
print("Square of 5:", square(5))  # Output: 25

#Map function iterable
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared Numbers using map:", squared_numbers)  # Output: [1, 4