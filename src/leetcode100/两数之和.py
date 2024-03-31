from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # l = len(nums)
        # for i in range(l):
        #     for j in range(i+1, l):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        hashtable = {} # is faster than dict()...
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [i, hashtable[target - num]]
            hashtable[num] = i
        return []
