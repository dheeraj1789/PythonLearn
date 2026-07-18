#Learn how to handle errors in Python by using try and except blocks. This allows you to catch exceptions and handle them gracefully without crashing your program.
#Basic error handling
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.") 
except Exception as e:
    print("An unexpected error occurred:", str(e))  
else:
    print("Division successful.")
#finally:
   # print("Execution completed  .")

# Try to read a file that does not eist

try:
    with open("bio.txt","r") as file:
       data = file.read()
except Exception as e:
    print("File does nt exist")
else:
    print("data is",data)
finally:
    print("Data printed")

    