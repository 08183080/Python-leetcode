# from types import List
"""
如何学好一门编程语言?
(1) 编程语言的语法本身
(2) 编程语言去实现【算法和数据结构】
(3) 编程语言的系统调用和系统的交互
"""

class NumArray:
    """
    但是超时。。。
    """
    def __init__(self, nums: list[int]):
        self._nums = nums

    def update(self, index: int, val: int) -> None:
        self._nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        ans = 0
        l = left
        r = right
        while l <= r:
            ans += self._nums[l]
            l += 1
        return ans

if __name__ == "__main__":
    # Your NumArray object will be instantiated and called as such:
    nums = [1, 3, 5]
    index = 1
    val = 2
    left = 0
    right = 2

    obj = NumArray(nums)
    obj.update(index,val)
    param_2 = obj.sumRange(left,right)
    print(param_2)