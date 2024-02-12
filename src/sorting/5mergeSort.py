from typing import List

nums = [1, 33, 2, 24, 8, 99, 100, 1, 2]

def merge_sort(nums: List[int]):
    if len(nums) < 2:
        return nums
    middle = len(nums) // 2
    left, right = nums[0: middle], nums[middle:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left: List[int], right: List[int]):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

if __name__ == "__main__":
    res = merge_sort(nums=nums)
    print(res)