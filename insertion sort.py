arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
inp = int(input("ienteger"))
arr.append(inp)
def InsertionSort(lst):
    for i in range(1, len(lst)):
        val_to_insert = lst[i]
        insert_spot = i
        while insert_spot > 0 and lst[insert_spot - 1] > val_to_insert:
            lst[insert_spot] = lst[insert_spot - 1]
            insert_spot -= 1
        lst[insert_spot] = val_to_insert
    return lst
print(InsertionSort(arr))