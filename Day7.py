#List is an ordered collection of items 
# which can be of any type. It is mutable and 
# allows duplicate elements. 
# Lists are defined using square brackets [].
fruits = ["apple", "banana", "cherry", "date"]  
numbers = [1, 2, 3, 4, 5]   
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
mixed_list = [1, "apple", 3.14, True]
print("last Fruits:", fruits[-1])
print("last Numbers:", numbers[-1])
print("last Days:", days[-1])
print("last Mixed List:", mixed_list[-1])
print("Days slicing", days[1:4])  # Output: ['Tuesday', 'Wednesday', 'Thursday']

#Basic List Operations
fruits.append("elderberry")  # Add an item to the end of the list
print("Fruits after append:", fruits)
numbers.remove(3)  # Remove an item from the list
print("Numbers after remove:", numbers)     
numbers.sort()  # Sort the list in ascending order
print("Numbers after sort:", numbers)       
numbers.reverse()  # Reverse the order of the list
print("Numbers after reverse:", numbers)
numbers.insert(2, 10)  # Insert an item at a specific index
print("Numbers after insert:", numbers) 
numbers.pop()  # Remove and return the last item from the list
print("Numbers after pop:", numbers)
#numbers.push(20)  # Add an item to the end of the list
print("Numbers after push:", numbers)

#List Comprehension
squared_numbers = [x**2 for x in range(1, 6)]
print("Squared Numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]

#Even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even Numbers:", even_numbers)  # Output: [2, 4, 6, 8, 10]

#Convert to uppercase
uppercase_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase Fruits:", uppercase_fruits)  # Output: ['APPLE', 'BANANA', 'CHERRY', 'DATE', 'ELDERBERRY']         


#tuple is an ordered collection of items which can be of any type.
#Tuples are immutable, meaning their elements cannot be changed after creation.
#Tuples are defined using parentheses ().
my_tuple = (1, 2, 3, 4, 5)
print("First Element:", my_tuple[0])  # Output: 1
print("Last Element:", my_tuple[-1])  # Output: 5
#listslicing

nums=[10, 20, 30, 40, 50]
print("Sliced List:", nums[1:4])  # Output: [20, 30, 40]        
print("Sliced List with step:", nums[::2])  # Output: [10, 30, 50] 
print("Sliced List with negative step:", nums[::-1])  # Output: [50, 40, 30, 20, 10]    
#List Comprehension
squared_numbers = [x**2 for x in range(1, 6)]
print("Squared Numbers:", squared_numbers)  # Output: [1, 4,  
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even Numbers:", even_numbers)  # Output: [2, 4, 6, 8, 10]  

#Remove duplicates from a list

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

list_with_duplicates = [1, 2, 3, 2, 4, 1, 5]
list_without_duplicates = remove_duplicates(list_with_duplicates)
print("List without duplicates:", list_without_duplicates)  # Output: [1, 2, 3, 4, 5]

squared_numbers = [x**2 for x in range(1, 6)]
print("Squared Numbers:", squared_numbers)  # Output: [1, 4,

list = []
for i in range(1, 6):
    list.append(int(input(f"Enter number {i}: ")))
print("List of numbers:", list)
print("Sorted list:", list.sort())  # Output: List of numbers: [user input]
tuple=tuple(list)
print("Tuple of numbers:", tuple)  # Output: Tuple of numbers: (user input) 
print("First Element of tuple:", tuple[0]) 
 # Output: Sorted list: [user input]