import math

def isPrime(x):
    if x == 2 or x == 3:
        return True
    for i in range(2, int(math.sqrt(x))+1):
        if x % i== 0:
            return False
    return True

def primeDecomposition(x):
    if isPrime(x):
        return [x]
    decomp = []
    for i in range(2, x-1):
        if x%i == 0:
            if isPrime(i):
                decomp.append(i)
            else:
                decomp = decomp + primeDecomposition(i)
            j = x/i
            if isPrime(j):
                decomp.append(j)
            else:
                decomp = decomp + primeDecomposition(j)
            return decomp
    return []

solution = 1
for i in range(2, 20):
    decomp = primeDecomposition(i)
    temp = solution
    for d in decomp:
        if temp%d == 0:
            temp /= d
        else:
            solution = solution * d

print(solution)
