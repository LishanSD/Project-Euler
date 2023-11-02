from timeit import default_timer as timer

start = timer()

#----------------------------------#

def count(n):
    count = 0
    for i in range(1, int(n/2) + 1):
        if (n%i == 0):
            count += 1

    return count + 1

print(count(100000))

#----------------------------------#

end = timer()
print(end - start)