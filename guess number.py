import random


def guess_my_number():
    k = random.randint(0, 100)
    while True:
        a = int(input("enter a number:"))

        if k>a:
            print("too small")
        elif k<a:
            print ("too big")
        else:
            print("you win")
            break
guess_my_number()
