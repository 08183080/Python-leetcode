from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a, b = 0, 0 # b counts numbers that not 0
        l = len(nums)
        for a in range(0, l):
            if nums[a] != 0:
                nums[b] = nums[a]
                b += 1
            else:
                continue
        for i in range(b, l):
            nums[i] = 0
        
if __name__ == "__main__":
    nums = [0,1,0,3,12]
    s = Solution()
    s.moveZeroes(nums=nums)
    print(nums)
