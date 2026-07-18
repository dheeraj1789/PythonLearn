with open("Day12.txt","r+") as fw:
    data = fw.read().splitlines()
    print(data)

#with open("Day12.txt","w") as fw:
    #fw.write("Hello, World!\n")
   # fw.write("This is my first time writing to a file in Python.")
    #print(data)
   # print(data[0])
   # print(data[1])
   # print("this is my first time reading from a file in Python.")
with open("Day12.txt","r") as fw:
    print("read line by line")
    for line in fw:
        print(line.strip())

#Writing lines by lines
lines = ["This is line 1\n", "This is line 2\n", "This is line 3\n"]
with open("Day12.txt", "w") as fl:
    fl.writelines(lines)

with open("sample.txt", "w") as file:
    file.write("This is a sample text file.\n")
    file.write("It contains multiple lines of text.\n")
    file.write("This is day 12 of python learning\n")
with open("sample.txt", "r") as file:

    data = file.read().splitlines()
    print("Reading the contents of the file:",data)