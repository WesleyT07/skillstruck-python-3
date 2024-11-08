#checkpoint
#this_list = ["Lion", "Elephant", "Giraffe", "Zebra", "Kangaroo", "Penguin", "Dolphin", "Eagle", "Shark", "Turtle"]
#def feeding(this_list):
#    if len(this_list) == 1:
#        animal = this_list[0]
#        print("The " + animal + " has been fed")
#    else:
#        mid = len(this_list) // 2
#        first_half = this_list[:mid]
#        second_half = this_list[mid:]
#        feeding(first_half)
#        feeding(second_half)
#feeding(this_list)
#Books and sequels
#books = [int(n) for n in input("Input a even list of numbers").split()]
#def pages(books):
#    if len(books) == 2:
#        numb = books[0]
#        print(books[0] + books[1])
#   else:
#        mid = len(books) // 2
#        first_half = books[:mid]
#        second = books[mid:]
#        pages(first_half)
#        pages(second)
#pages(books)
#pollinating Bees
flowers = [int(n) for n in input("How many blossoms are on the trees? ").split()]

def total_visits(flowers):
    if len(flowers) == 1:
        print(flowers[0] * 3, end=' ')
    else:
        print(flowers[0] * 3, end=' ')
        total_visits(flowers[1:])
total_visits(flowers)