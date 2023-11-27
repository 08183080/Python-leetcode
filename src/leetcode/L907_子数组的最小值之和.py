from typing import List
"""
单调栈
"""

MOD = 10 ** 9 + 7

class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        monoStack = []
        left = [0] * n
        right = [0] * n
        for i, x in enumerate(arr):
            while monoStack and x <= arr[monoStack[-1]]:
                monoStack.pop()
            left[i] = i - (monoStack[-1] if monoStack else - 1)
            monoStack.append(i)
        monoStack = []
        for i in range(n - 1, -1, -1):
            while monoStack and arr[i] < arr[monoStack[-1]]:
                monoStack.pop()
            right[i] = (monoStack[-1] if monoStack else n) - i
            monoStack.append(i)
        ans = 0
        for l, r, x in zip(left, right, arr):
            ans = (ans + l * r * x) % MOD
        return ans


if __name__ == "__main__":
    s = Solution()
