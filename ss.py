import random
ad = ""
for i in range(7):
    if i in (0, 1, 5, 6):
        ad += chr(random.randint(65, 90))
    elif i == 3:
        ad += "_"
    else:
        ad += str(random.randrange(100))
print(ad)
