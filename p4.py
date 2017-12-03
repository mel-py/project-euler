def isPalindrome(x):
    str_num = str(x)
    if str_num == str_num[::-1]:
        return True
    else:
        return False

def findPalindrome():
    for i in range(9999,1000,-1):
        for j in range(9999,1000,-1):
            if isPalindrome(i*j):
                return i*j

print(findPalindrome())
            
