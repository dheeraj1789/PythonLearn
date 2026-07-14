#Solid rectangle
rows = 7
cols = 8
def print_rectangle(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print("*",end=" ")
    print() 
    
rows = 5
#trangle
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print() 

#hallow ractangle

rows = 5
cols = 6
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#Revtangle with number
rows = 4    
cols = 5
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(j, end=" ")
    print()
    
#Hallow triangle
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    rows = 5

for i in range(rows, 0, -1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end=" ")
    
    # Print stars
    for k in range(2 * i - 1):
        print("*", end=" ")
    
    print()

rows = 5
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end=" ")
    print() 

    rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()