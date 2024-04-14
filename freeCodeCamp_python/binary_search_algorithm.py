import random
import time

def common_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    
    return -1

def binary_search(array, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(array) - 1 
    if high < low:
        return -1

    midpoint = (low + high)//2

    if target == array[midpoint]:
        return midpoint
    elif target < array[midpoint]:
        return binary_search(array, target, low, midpoint-1)
    else:
        return binary_search(array, target, midpoint+1, high)
    


if __name__ == '__main__':
    #making a list with unique sorted integers
    length = 10000
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))

    sorted_list = sorted(list(sorted_list))

    #calculating average time of common search
    start = time.time()
    for target in sorted_list:
        common_search(sorted_list, target)
    end = time.time()

    average_of_common = (end - start)/length
    print(f'Common search time: {average_of_common} seconds')

    #caculating average time of binary search
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()

    average_of_binary = (end - start)/length
    print(f'Binary search time: {average_of_binary} seconds')

    #shows time efficency of binary search over common
    print(f'Binary search {average_of_common/average_of_binary} times more efficient than common search')



