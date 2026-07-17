#Create a list of 5 favourite moviies

favorite_movies = ["Inception", "The Dark Knight", "Interstellar", "The Matrix", "Pulp Fiction"]
#adding at end of the list
favorite_movies.append("The Shawshank Redemption")
#Remove at index 2
favorite_movies.pop(2)
print("My favorite movies in reverse order:", favorite_movies[::-1])

numbers = [45, 12, 67, 3, 89, 24, 56]

# Do the following:
# 1. Sort the list
# 2. Find the maximum and minimum number
# 3. Create a new list with only even numbers from above
sorted_list = numbers.sort()
for num in numbers:
    if num % 2 == 0:
        even_numbers = [num for num in numbers if num % 2 == 0]
print("Sorted list:", numbers)
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))
print("Even numbers:", even_numbers)

#Create a dictionary with 5 key-value pairs representing your favorite books and their authors. Then, perform the following operations:
me = {"name": "Dheeraj",
      "age":34,
      "city":"Prayagraj",
      "skills":["Python","Java","C++"],
      "profession":"Software Engineer"}
print("My details:", me)
phonebook = {"Alice": "123-456-7890",
             "Bob": "987-654-3210",
             "Charlie": "555-555-5555",
             "David": "111-222-3333"}

#phonebook.("Eve", "444-444-4444")
print("Phonebook:", phonebook)
phonebook.update({"Alice": "999-999-9999"})
print("Updated phonebook:", phonebook)
phonebook.pop("Charlie")
print("Phonebook after removing Charlie:", phonebook)
print(f"Charlie's phone number: {phonebook.get('Charlie', 'Not found')}")
print("Phonebook after removing Charlie:", phonebook)
print(f"Charlie's phone number: {phonebook.get('Charlie', 'Not found')}")           
students = {
    "Rahul": {"Math": 85, "Science": 90, "English": 78},
    "Priya": {"Math": 92, "Science": 88, "English": 95}
}
students["Amit"] = {"Math": 75, "Science": 80, "English": 70}
print("Students and their scores:", students)

average_scores_for_Amit  = students["Amit"].fromkeys(students["Amit"], sum(students["Amit"].values()) / len(students["Amit"]))
print("Average scores for Amit:", average_scores_for_Amit)   

squares = []
for i in range(10):
    squares.append(i ** 2)
print("Squares of numbers from 0 to 9:", squares)   

even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
print("Squares of even numbers from 0 to 9:", even_squares)

students = [("Alice", 85), ("Bob", 90), ("Charlie", 78), ("David", 92)]
students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
print("Students sorted by scores:", students_sorted)