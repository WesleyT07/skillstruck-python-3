#checkpoint
#my_list = [[40, 45, 50], [6, 7, 8], [100, 200, 300], [50, 60, 70], [9, 0, 1]]
#rows = 5
#cols = 3
#for i in range(rows):
#    for j in range(cols):
#        my_list[i][j] = my_list[i][j] + 3
#print(my_list)
#Multiply List Values
#my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]
#num = int(input("Number: "))
#row = 4
#cols = 3
#for i in range(row):
#    for j in range(cols):
#        my_list[i][j] = my_list[i][j] * num
#print(my_list)
rows = 4
cols = 3
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
largest = 0
my_list = [[0, 1, x], [10, 15, y], [100, 200, 300], [5, 6, z]]
for i in range(rows):
    for j in range(cols):
        if my_list[i][j] > largest:  
            largest = my_list[i][j]
        
print(largest)