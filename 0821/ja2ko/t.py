






import random
import time
import datetime


def lock_mg():

    while True:
        return random.choice(["lock msg","msg"])



result = lock_mg()
def dd(response,func,maxx):
    num = 0
    num += 1
    print(result)
    if num < maxx:
        if response != "lock msg":

            return result
        else:

            dd(response,func,maxx)





# dd(result,lock_mg(),5)


while True:
    next(lock_mg)