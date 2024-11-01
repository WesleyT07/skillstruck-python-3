#checkpoint
#rows = 5
#cols = 3
#list = []
#for i in range(rows):
#    col = []
#    for j in range(cols):
#        col.append(5)
#    list.append(col)
#print(list)
#name generator
#fnames = ['jimmy', 'josh', 'ryan', 'harry']
#lnames = ['thomas', 'carter', 'perez', 'gonzo']
#list = []
#for f in fnames:
#    col = []
#    for l in lnames:
#        col.append(f + " " + l)
#   list.append(col)
#print(list)
#Fruit blender
fruits = ["apple", "grape", "peach", "cinnamon", "vanilla"]
mixer = input("Fruits:").split()
mix = []
for m in mixer:
    col = []
    for f in fruits:
        col.append(m + " " + f)
    mix.append(col)
print(mix)
