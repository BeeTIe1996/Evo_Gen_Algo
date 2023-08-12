import random

def point_mut(Arr, N):
    per = 30
    if random.randrange(100) < per:
        index = random.choice(Arr)
        temp = [i for i in range(N)]
        a1 = random.choice(temp)
        if a1 == len(temp)-1:
            Arr[index][a1], Arr[index][a1-1] = Arr[index][a1-1], Arr[index][a1]
        else:
            Arr[index][a1], Arr[index][a1+1] = Arr[index][a1+1], Arr[index][a1]
        return Arr, index
    else:
        index = -1
        return Arr, index

def saltation(Arr, N):
    per = 30
    if random.randrange(100) < per:
        temp = [i for i in range(N)]
        a1 = random.choice(temp)
        temp.remove(a1)
        a2 = random.choice(temp)
        Arr[a1], Arr[a2] = Arr[a2], Arr[a1]
        return Arr
    else:
        return Arr