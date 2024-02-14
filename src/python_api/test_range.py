from random import randint

nums = [randint(10, 20) for i in range(10)]
print('[*] array: ',nums)

n = len(nums)//2 - 1
print('[*] half len: ', n)

for i in range(n, -1, -1):
    print(i, end=' ')
print()

for i in range(n+1, 2*n+2):
    print(i, end=' ')
print()