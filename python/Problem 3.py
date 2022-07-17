import math

def largestPrimeFactor(n):
    largestPrime = 2

    while n % 2 == 0:
        n /= 2

    for i in range(2, int(math.sqrt(n)), 2):
        while n % i == 0:
            largestPrime = i
            n /= i

    if n > 2:
        largestPrime = n

    return largestPrime

print(largestPrimeFactor(600851475143))