def function_name():
    print("This is a function.")

def greet():
    print("Hello welcome to the function")

function_name()
greet()
greet()

def greet_user(name):
    print(f"Hello {name}, welcome to the function")

greet_user("John")  
greet_user("Alice")

#function with return value

def add_numbers(a, b):
    return a + b    
print ("addition=", add_numbers(5,3))
print ("addition=", add_numbers(10,20))

def calculate_area(length, width):
    area = length * width
    return area
print("Area of rectangle:", calculate_area(5, 3))

#default argument
def greet_user(name="Guest"):
    print(f"Hello {name}, welcome to the function")

greet_user()  # Uses default value "Guest"
greet_user("Alice")  # Uses provided value "Alice"

#You can pass arguments by name (order doesn’t matter).

def student_info(name, age, grade):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

student_info("John", 20, "A")
student_info(age=22, grade="B",name="Alice")

# multiple positional arguments
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print("Sum:", sum_numbers(1, 2, 3, 4, 5))

#Multiple keyword arguments

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="John", age=25, city="New York") 

def interview_eligibility(age, experience):
    if age >= 18 and experience >= 2:
        return "Eligible for interview"
    elif age < 18:
        return "Not eligible for interview"
    elif experience < 2:       
        return "Not eligible for interview"
    
    interview_eligibility(20, 3)  # Output: "Eligible for interview"  
