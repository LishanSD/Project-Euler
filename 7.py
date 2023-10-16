# Problem 7

from math import sqrt


def is_prime(n):
    if (n ==1):
        return False
    
    for i in range(2, int(sqrt(n)) + 1):
        if (n%i == 0):
            return False
    
    return True


def main():
    number = 0
    count = 0

    while (count < 10001):
        number += 1
        if (is_prime(number)):
            count += 1

    print(number)    


if __name__ == "__main__":
    main()