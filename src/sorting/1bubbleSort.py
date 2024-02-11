from time import time
from typing import List

nums = [1, 2, 56, 3, 11, 34, 99]

def time_func(func, *args, **kwargs):
    """
    Time the execution of a function with params
    """
    start = time() 
    output = func(*args, **kwargs)
    end = time()
    if int(end - start) > 0:
        print(f'{func.__name__} runtime: {(end - start):0.4f}s')
    else:
        print(f'{func.__name__} runtime: {(end - start):0.4f}s')
    return output

def bubble_sort(nums: List[int]):
    n = len(nums)
    for i in range(1, n):
        for j in range(0, n - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

if __name__ == "__main__":
    output = time_func(bubble_sort, nums)
    print(output)