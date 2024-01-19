
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]

        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


x = [10, 5, 100, 43, 16, 18, 1, 4, 3, 0, 50]

print(quicksort(x))
