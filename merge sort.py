arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
inp = int(input("integer"))
arr.append(inp)
def MergeSort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    left_sorted = MergeSort(left_half)
    right_sorted = MergeSort(right_half)
    return merge(left_sorted, right_sorted)
def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list
print(MergeSort(arr))