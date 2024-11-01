#Checkpoint
#rows = 3
#pets = ['dog', 'cat', 'mouse', 'rat', "liazrd"]
#loop = [[p for p in pets] for i in range(rows)]
#print(loop)
#Multiply by the number of rows
#rows = int(input("rows:"))
#mylist = [1, 2, 3, 4, 5]
#list = [[n * rows for n in mylist] for i in range(rows)]
#print(list)
#weather watcher
rows = (input("weather:")).split()
cols = ['windy', 'breezy', 'calm']
list = []
for row in rows:
    inner_list = []
    for col in cols:
        inner_list.append(row + " " + col)
    list.append(inner_list)
print(list)