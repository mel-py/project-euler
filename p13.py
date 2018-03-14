file = open("p13num.txt", 'r')
num = 0
for line in file:
    num += int(line)
print(num)
