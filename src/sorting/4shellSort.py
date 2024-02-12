import math
from typing import List

nums = [1, 22, 3, 17, 99, 96, 23, 11, 1]

def shell_sort(nums: List[int]) -> List[int]:
    gap = 1
    while (gap < len(nums) / 3):
        gap = gap * 3 + 1
    # print(gap)
    while gap > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            j = i - gap
            while j >= 0 and nums[j] > temp:
                nums[j + gap] = nums[j]
                j -= gap
            nums[j + gap] = temp
        gap = math.floor(gap / 3)
        # print(gap)
    return nums

if __name__ == "__main__":
    shell_sort(nums=nums)  
    print(nums)