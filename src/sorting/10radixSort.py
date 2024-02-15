import random
from typing import List

"""
begin: https://www.programiz.com/dsa/radix-sort

1. find the max num, count its digits
2. go through each significant place one by one
"""

nums = [random.randint(0, 1000) for i in range(10)] # an array, len = 10, value = [0, 9]
print('[*] original nums array:', nums)

def count_sort(num: List[int], place: int):
    size = len(nums)
    output = [0] * size
    count = [0] * size

    # calculate count of elements
    for i in range(0, size):
        index = nums[i] // place
        count[index % 10] += 1
    print(f'{place}\t: {count}')
    
    # why calculate cumulative count? to get pos
    for i in range(1, 10):
        count[i] += count[i - 1]
    print(f'{place} added\t: {count}')

    i = size - 1
    while i >= 0:
        index = nums[i] // place
        output[count[index % 10] - 1] = nums[i]
        count[index % 10] -= 1
        i -= 1
    print(f'final count: {count}')
    
    for i in range(0, size):
        nums[i] = output[i]
    print(f'{nums}')

def radix_sort(nums: List[int]):
    max_value = max(nums) # get max value

    place = 1
    while max_value // place > 0:
        count_sort(nums, place)
        place = place * 10

if __name__ == "__main__":
    radix_sort(nums=nums)
    print('[*] finally sorted array: ', nums)