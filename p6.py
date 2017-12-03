def sumOfSquares():
    total = 0
    for i in range(1, 101):
        total += i ** 2
    return total

def squareOfSums():
    total = 0
    for i in range(1, 101):
        total += i
    total = total ** 2
    return total

solution = squareOfSums() - sumOfSquares()
print(solution)
