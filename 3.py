# Problem 3

from math import sqrt

def is_prime(n):
    if (n ==1):
        return False
    
    for i in range(2, int(sqrt(n)) + 1):
        if (n%i == 0):
            return False
    
    return True


number = 600851475143

if (is_prime(number)):
    print(number)
else:
    largest_factor = 0
    i = 1
    while (number/i >= sqrt(number)):
        if (number%i == 0):
            if (is_prime(number/i)):
                largest_factor = number/i
                break
            elif (is_prime(i)):
                largest_factor = i
        i += 1

    print(largest_factor)