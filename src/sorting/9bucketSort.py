from typing import List
from random import random

"""
buckets sort
ref: https://www.programiz.com/dsa/bucket-sort
"""

nums = [round(random(), 2) for i in range(10)]
print('[*] original float array:',nums)

def bucket_sort(nums: List[float]):
    res = []
    buckets = []
    n = len(nums)
     
    for i in range(n):
        buckets.append([])

    for num in nums:
        i = int(10 * num)
        buckets[i].append(num)
    
    for i in range(n):
        buckets[i] = sorted(buckets[i]) # quicksort
    
    for i in range(n):
        if buckets[i]:
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
    return res

if __name__ == "__main__":
    res = bucket_sort(nums=nums)
    print('[*] sorted array: ', res)
