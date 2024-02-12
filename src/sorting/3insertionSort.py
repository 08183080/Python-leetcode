from typing import List

nums = [1, 34, 2, 9, 15, 26, 33, 999, 23, 1]

def insert_sort_debug(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        print(f'[{i}] begins ....')
        pre = i - 1
        print(f'i is {i}, and pre is {pre}...')
        curval = nums[i]
        print(f'currrent value is {curval}')
        while pre >= 0 and nums[pre] > curval:
            print(f'enter the insertion loop...')
            print(f'nums[pre] is {nums[pre]}, pre is {pre}')
            nums[pre + 1] = nums[pre]
            print(f'nums[pre+1] is {nums[pre + 1]}')
            pre -= 1
            print(f'pre = pre -1, then {pre}')
        nums[pre + 1] = curval
        print(f'finally nums[pre+1] is {nums[pre + 1]}\n\n')
    return nums

def insert_sort(nums: List[int]):
    for i in range(len(nums)):
        pre = i - 1
        curval = nums[i]
        while pre >= 0 and nums[pre] > curval:
            nums[pre + 1] = nums[pre]
            pre = pre - 1
        nums[pre + 1] = curval
    return nums

if __name__ == "__main__":
    insert_sort_debug(nums=nums)
    print(nums)