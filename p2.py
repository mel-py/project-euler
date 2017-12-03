even_terms = []

x = 1
y = 1

while (y < 4000000):
    z = x+y
    x = y
    y = z

    if y % 2 == 0:
        even_terms.append(y)

    print(y)

total_sum = 0
for i in even_terms:
    total_sum += i

print("The sum is: ", total_sum)
