# Problem 10

from math import sqrt


def count1(n):
    count = 0
    for i in range(1, int(n/2) + 1):
        if (n%i == 0):
            count += 1

    return count + 1


def count2(n): # more efficient (there is a error, it should be corrected)
    count = 0
    for i in range(1, int(sqrt(n)) + 1):
        if (n%i == 0):
            count += 2
    if (n == sqrt(n)**2):
        count -= 1
    
    return count


def count3(n): # more efficient
    count = 0
    i = 1
    k = n

    if (n == 1):
        return 1
    else:
        while (i < k):
            if (n%i == 0):
                k = n/i
                if (i == k):
                    count += 1
                else:
                    count += 2
            i = i + 1

        return count


if __name__ == "__main__":
    n = 0
    i = 0
    while True:
        i += 1
        n = (i*(i+1))/2

        if (count3(n) > 500):
            print(n)
            break