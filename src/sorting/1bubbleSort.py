from typing import List

nums = [1, 2, 56, 3, 11, 34, 99]

def bubble_sort(nums: List[int]):
    n = len(nums) 
    for i in  range(1, n):
        for j in range(0, n - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

if __name__ == "__main__":
    bubble_sort(nums=nums)
    print(nums)