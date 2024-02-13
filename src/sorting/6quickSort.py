import random
from typing import List

nums = [random.randint(0, 100) for i in range(10)]
print('[*] original nums array:',nums)

def quick_sort(nums: List[int]) -> List[int]:
    """
    code inspired by [alogitithm graph books]
    """
    if len(nums) < 2:
        return nums
    pivot = nums[0]
    left = [i for i in nums[1:] if i < pivot]
    right = [i for i in nums[1:] if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right) 

if __name__ == "__main__":
    res = quick_sort(nums=nums)
    print('[*] after quick sort: ',res)