# Problem 6

n = 100
sum_1 = 0
sum_2 = 0

for i in range(1, n+1):
    sum_1 += i**2
    sum_2 += i

print(sum_2**2 - sum_1)