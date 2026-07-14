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


