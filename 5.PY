# Problem 5

flag = False
i = 0

while (flag == False):
    i += 20
    count  = 0
    
    for j in range(20, 0, -1):
        if (i%j != 0):
            break
        else:
            count += 1
    
    if (count == 20):
        flag = True
        print(i)