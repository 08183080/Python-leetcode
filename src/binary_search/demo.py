from typing import List

nums = [1, 3, 5, 7, 19, 23]

def binary_find(nums: List[int], target: int):
    """
    find the index of the nums list, if not, return -1
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    # print(f'after the loop, left value is {left}, right value is {right}')
    if nums[left] == target:
        return left
    return -1 

if __name__ == "__main__":
    print(binary_find(nums, 24))
    print(binary_find(nums, -1))
    print(binary_find(nums, 7))
