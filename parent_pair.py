import random

from operators import getWayLenght

def panmix(arr):
    p1 = random.choice(arr)
    "arr.remove(p1)"
    p2 = random.choice(arr)
    return p1,p2

def negative_acc(Arr):
    p = 30
    if random.randrange(100) < p:
        cc = []
        for k in range(len(Arr)):
            cc.append(getWayLenght(Arr[k]))

        maxc = max(cc)
        minc = min(cc)

        p1 = Arr[cc.index(maxc)]
        p2 = Arr[cc.index(minc)]

    else:
        p1 = random.choice(Arr)
        Arr.remove(p1)
        p2 = random.choice(Arr)
    return p1, p2
