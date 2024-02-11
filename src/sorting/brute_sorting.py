from typing import List

nums = [1, 3, 2, 5, 23, 8, 99, 36]

def brute_sorting(nums: List[int]):
    """
    sort nums array
    """
    n = len(nums)
    for i in range(0, n):
        for j in range(i, n):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

if __name__ == "__main__":
    brute_sorting(nums=nums)
    print(nums)