
def isPalindrome(x):
    xAsString = str(x)
    return xAsString[::-1] == xAsString


largest = 0

for x in range(999, 99, -1):
    left = x
    right = 999

    while right > 100:
        if isPalindrome(left * right) is True:
            if(largest < left * right):
                largest = left * right

        right -= 1

print(largest)