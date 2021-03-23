import random

c = random.randint(1, 1001)
for r in range(7):
    g = int(input())
    while g != c:
    
        count = 0
        if g > c:
            print("Too big")
        elif g < c:
            print("Too small")
            break
        else:
            print("You Win")
        count = count + 1
    print(count)
