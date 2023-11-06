from functools import reduce

def get_bitwise(words: str) -> int:
    """
    get_bitwise() 函数应该可以正确地计算给定字符串中所有字符的按位或操作，并返回结果作为整数。
    请注意，结果是一个整数，表示所有字符的位运算结果。
    """
    return reduce(lambda x, y: x | 1 << (ord(y) - ord('a')), words, 0)

if __name__ == "__main__":
    words = ["abcd", "efj"]
    
    print(bin(get_bitwise(words[0])))
    print(bin(get_bitwise(words[1])))