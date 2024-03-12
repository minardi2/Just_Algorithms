
x = [10, 25, 15, 20, 5, 30]
z = [12, 12, 11, 10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    newarray = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newarray.append(arr.pop(smallest))
    return newarray

print(find_smallest(x))

print(selection_sort(x))
print(selection_sort(z))
