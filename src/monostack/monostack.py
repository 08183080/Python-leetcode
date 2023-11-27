"""
2023-11-27
实现单调栈: 单调递增(减)栈
返回当前元素右边比它大的最近的元素 数值/下标
"""
from typing import List

def monotic_stack(nums: List[int]):
    """
    I: [1, 2, 5, 3, 7, 4]
    O: [1, 2, 4, 4, -1, -1]
    """
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[i] > stack[-1]:
            top = stack.pop()
            res[top] = i
        stack.append(i)
    
    return res

if __name__ == "__main__":
    nums = [1, 2, 5, 3, 7, 4]
    res = monotic_stack(nums)
    print(res)