from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        l = 0
        n = len(nums)
        while l < n:
            if nums[l] % 2 or nums[l] > threshold:
                l += 1
                continue
            start = l
            l += 1
            while l < n and nums[l] <= threshold and (nums[l - 1] % 2 != nums[l] % 2):
                l += 1
            ans = max(ans, l - start)
        return ans

if __name__ == "__main__":
    s = Solution()
    nums = [3,2,5,4]
    threshold = 5
    ans = s.longestAlternatingSubarray(nums, threshold)
    print(ans)