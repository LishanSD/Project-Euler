# Problem 10

from math import sqrt


def is_prime(n):
    if (n == 0 or n == 1):
        return False
    
    for i in range(2, int(sqrt(n)) + 1):
        if (n%i == 0):
            return False
    
    return True


if __name__ == "__main__":
    sum = 0
    for i in range(2000000):
        if (is_prime(i)):
            sum += i
    
    print(sum)