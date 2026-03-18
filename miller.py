import secrets as s

_SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]

def stringToInt(string):
    digit_list = []
    for char in string:
        if char.isdigit():
            digit_list.append(int(char))
    number = 0
    power = len(digit_list)-1

    for digit in digit_list:
        number += digit*pow(10, power)
        power -= 1
    return number

def _millerRabinTest(n, base=2):
    d = n - 1
    r = 0
    while (d & 1) == 0:  # Bitwise check for even
        d >>= 1  # Bitwise divide by 2
        r += 1
    
    x = pow(base, d, n)
    if (x == 1 or x == n - 1):
        return True
    
    for _ in range(r - 1):
        x = pow(x, 2, n)
        
        if (x == n-1):
            return True
    return False

def mil(n, times=16):
    if (n < 2):
        return False
    
    # Trial division against small primes for quick composite rejection
    for p in _SMALL_PRIMES:
        if n % p == 0:
            return n == p  # True only if n is the prime itself
    
    for _ in range(times):
        base = s.randbelow(n - 3) + 2  # Random in [2, n-2]
        if not _millerRabinTest(n, base):
            return False
    return True

def nextPrime(n, times=16):
    i = n
    if (i % 2 == 0):
        i += 1
    
    while True:
        if mil(i, times):
            return i
        i += 2