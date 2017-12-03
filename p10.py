import math

def isPrime(x):
    if x == 2 or x == 3:
        return True
    for i in range(2, int(math.sqrt(x))+1):
        if x % i== 0:
            return False
    return True

primes = []
for i in range(2000000):
    if isPrime(i):
        primes.append(i)

a = 0
for p in primes:
    a += p
print(a)
