import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True

n = 600851475143
sqrt_n = int(math.sqrt(n))

largest_prime = 0
for i in range(2, sqrt_n):
    if (n % i == 0):
        if isPrime(i):
            largest_prime = i

print(largest_prime)
                
