import random
a = random.uniform(1,100)
b = random.uniform(-1,-100)
number = int(input('enter number:'))
if number == 0:
    print("0")
if number > 0:
    print(int(a) )
if number < 0:
    print(int(b) )