import math

def numDivisors(number):
    num = 0
    for i in range(1, int(math.sqrt(number))+1):
        if i * i == number:
            num += 1
        elif number % i == 0:
            num += 2
    return num

triangle = 0
i = 1
while (numDivisors(triangle) < 500):
   triangle += i
   i += 1
print(triangle)
    
