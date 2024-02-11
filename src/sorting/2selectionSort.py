from typing import List

nums = [1, 33, 2, 6, 19, 100]

def select_sort(nums: List[int]):
    n = len(nums)
    for i in range(0, n-1):
        for j in range(i, n):
            min = i
            if nums[j] < nums[i]:
                min = j
            if min != i:
                nums[i], nums[min] = nums[min], nums[i]
    return nums

if __name__ == "__main__":
    ans = select_sort(nums=nums)
    print(ans)