import random
from typing import List

"""
begin: https://www.programiz.com/dsa/radix-sort
"""

nums = [random.randint(0, 100) for i in range(10)] # an array, len = 10, value = [0, 9]
print('[*] original nums array:', nums)

def radix_sort(nums: List[int]):
    n = len(nums)
    