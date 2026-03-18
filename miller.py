import secrets as s

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

def _millerRabinTest(n, base):
    d = n - 1
    s = 0
    
    while (d % 2 == 0):
        d = d//2
        s += 1
    
    x = pow(base, d, n)
    if (x == 1 or x == n - 1):
        return True
    
    for _ in range(s - 1):
        x = pow(x, 2, n)
        
        if (x == n-1):
            return True
    return False

def mil(n, times):
    if (n < 2):
        return False
    if (n in [2, 3, 5, 7]):
        return True
    if (n % 2 == 0):
        return False
    
    test = [(s.randbelow(n-4) + 2) for _ in range(times)]
    
    if all([_millerRabinTest(n, i) for i in test]):
        return True
    return False

def nextPrime(n, times):
    i = n
    if (i % 2 == 0):
        i += 1
    
    while True:
        if mil(i, times):
            return i
        i += 2

        
        