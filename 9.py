# Problem 9

if __name__ == "__main__":
    a = 1
    b = a + 1
    flag = False

    while (a**2 + b**2 != (1000 - a - b)**2):
        for b in range(a+2, 1000-a+1):
            if (a**2 + b**2 == (1000 - a - b)**2):
                flag = True
                break
        
        if (flag == False):
            a += 1
            b = a + 1

    c = (a**2 + b**2)**(1/2)

    print(a*b*c)