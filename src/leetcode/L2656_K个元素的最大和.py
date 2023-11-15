import heapq
from typing import List

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        """
        维持一个优先级队列, 降序排序...
        每次把队首的元素拿出来, 然后+1再放回去...
        """
        ans = 0
        q = [-i for i in nums] # python默认是最小堆, 负数表示最大堆
        heapq.heapify(q)
        while k > 0:
            x = heapq.heappop(q)
            ans += -x
            heapq.heappush(q, x-1)
            k -= 1
        return ans