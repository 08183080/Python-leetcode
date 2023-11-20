from typing import List
"""
2023-11-20 晚上...
软件测试中的test oracle相当于人工智能中的ground truth
如何做出真正能解决问题实际效应的成果?
提升认知, 破除我执...

我需要一个 交谈语音2文字 工具...
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
                            dp[i-1] + nums[i] , dp[i-1] > 0
        动态规划: dp[i] = 
                            nums[i] , dp[i-1] < 0
                 dp[0] = nums[0]
        """
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)

def test():
    s = Solution()
    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    nums2 = [1]
    nums3 = [5,4,-1,7,8]

    assert s.maxSubArray(nums1) == 6
    assert s.maxSubArray(nums2) == 1
    assert s.maxSubArray(nums3) == 23

if __name__ == "__main__":
    test()