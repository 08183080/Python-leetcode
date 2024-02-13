import random
from typing import List

nums = [random.randint(0, 100) for i in range(10)]
print('[*] original nums array:',nums)

def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    left, right = nums[0: mid], nums[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left: List[int], right: List[int]) -> List[int]:
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    while left:
        res.append(left.pop(0))
    while right:
        res.append(right.pop(0))
    return res

if __name__ == "__main__":
    res = merge_sort(nums=nums)
    print('[*] after merge sort: ', res)