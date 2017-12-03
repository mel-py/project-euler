primes = [2]
limit = 10001

i = 1
while len(primes) < limit:
    isPrime = True
    i += 1
    for p in primes:
        if i%p == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)

print(primes[limit-1])
