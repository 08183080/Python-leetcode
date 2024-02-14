import heapq
import random
from typing import List

"""
Steps:
(1) build max-heap, use heapify()
(2) on maxheap, swap and heapify to get sorted array!
Refs:
https://www.programiz.com/dsa/heap-sort
"""
nums = [random.randint(0, 100) for i in range(10)]
print('[*] original nums array: ', nums)

def heap_sort_stl(nums: List[int]) -> List[int]:
    heapq.heapify(nums)
    res = []
    while nums:
        res.append(heapq.heappop(nums))
    return res

def heap_sort(nums: List[int]):
    n = len(nums)

    for i in range(n // 2 - 1, -1, -1):
        h = heapify(nums, n, i) # build max-heap successfully!

    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)
    return nums

def heapify(nums, n, i):
    max = i
    l = 2 * i + 1
    r = l + 1
    if l < n and nums[i] < nums[l]:
        max = l
    if r < n and nums[max] < nums[r]:
        max = r
    if max != i:
        nums[i], nums[max] = nums[max], nums[i]
        heapify(nums, n, max)
    return nums

if __name__ == "__main__":
    res = heap_sort(nums=nums)
    print('[*] after heap sort: ', res)