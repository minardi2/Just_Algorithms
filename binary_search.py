
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def bin_search(list, item):
    low = 0
    high = len(list)-1
    if item in my_list:
        iter_counter = 0
        while low <= high:
            mid = int((low + high)/2)
            guess = list[mid]
            iter_counter += 1
            if guess == item:
                print(f'Item: {item} is on position {mid}')
                print(f'Number of iteration: {iter_counter}')
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
    else:
        print(f'The item: {item} is not in your list')

bin_search(my_list, 3)