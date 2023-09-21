# Problem 4

flag = False

for i in range(999*999, 0, -1):
    if (str(i) == str(i)[::-1]):
        for j in range(999, 0, -1):
            if (i/j > 999):
                break
            elif (i%j == 0):
                flag = True
                print(i)
                break

    if (flag == True):
        break