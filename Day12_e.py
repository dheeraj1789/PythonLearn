with open("my_bio.txt", "w") as file:
    file.write("Name: John Doe\n")
    file.write("Age: 30\n")
    file.write("Occupation: Software Developer\n")
    file.write("Hobbies: Reading, Traveling, Coding\n")
with open("my_bio.txt", "r") as file:
    data = file.read().splitlines()
    print("Reading the contents of the file:",data) 

#Excercise: 3 ask user to enter 5 friends

with open("friends.txt", "w") as file:
    for i in range(5):
        friend_name = input(f"Enter the name of friend {i + 1}: ")
        file.write(friend_name + "\n")      
with open("friends.txt", "r") as file:
    data = file.read().splitlines()
    print("List of friends:", data) 