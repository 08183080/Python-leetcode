import random
from typing import List

nums = [random.randint(0, 9) for i in range(10)] # an array, len = 10, value = [0, 9]
print('[*] original nums array:', nums)

def count_sort(nums: List[int]):
    n = len(nums)
    count = [0] * n
    for num in nums:
        count[num] += 1

    j = 0
    for i in range(10):
        while count[i] > 0:
            nums[j] = i
            j += 1
            count[i] -= 1
    return nums

if __name__  == "__main__":
    res = count_sort(nums=nums)
    print('[*] final nums array: ', res)    

