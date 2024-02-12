"""
greattes common divide number
gcd(4, 2) == 2
gcd(19, 1) == 1
"""
def gcd_loop(a: int, b: int):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

def gcd(a: int, b: int):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == "__main__":
    assert gcd(4, 2) == 2
    assert gcd(3, 1) == 1
    assert gcd(88, 6) == 2