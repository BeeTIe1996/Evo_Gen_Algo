import random

def cycle(p1,p2):
    cc = []
    tempc = []
    visited = []

    while len(visited) != len(p1):
        ind=0
        while ind in visited:
            ind+=1
        tempc.append(p1[ind])
        while p2[ind] not in tempc:
            visited.append(ind)
            tempc.append(p2[ind])
            ind = p1.index(p2[ind])
        cc.append(tempc)
        tempc=[]
    return cc


def ord_cross(p1, p2, N):
    arr = []
    for i in range(N):
        arr.append(i)
    a1 = random.choice(arr)
    arr.remove(a1)
    a2 = random.choice(arr)
    if a1 > a2:
        a1, a2 = a2, a1
    child = [-1 for i in range(N)]
    for i in range(a1-1, a2):
        child[i] = p1[i]
    for i in range(a2-1,N):
        for j in range(a2-1,N):
            if p2[j] not in child:
                child[i] = p2[j]
                break
        for j in range(a1):
            if p2[j] not in child:
                child[i] = p2[j]
                break
    for i in range (a1):
        for j in range(a2-1,N):
            if p2[j] not in child:
                child[i] = p2[j]
                break
        for j in range(a1):
            if p2[j] not in child:
                child[i] = p2[j]
                break
    return child

    
def part_cross(p1, p2, N):
    arr = []
    for i in range(N):
        arr.append(i)
    a1 = random.choice(arr)
    arr.remove(a1)
    a2 = random.choice(arr)
    if a1 > a2:
        a1, a2 = a2, a1
    child = [-1 for i in range(N)]
    for i in range(a1-1, a2):
        child[i] = p1[i]
    cc = cycle(p1,p2)
    for k in range(len(child)):
        if child[k] == -1:
            for i in range(len(cc)):
                for j in range(len(cc[i])):
                    if p1[k] in cc[i]:
                        if cc[i][j]==p1[k]:
                            while cc[i][j+1] in child:
                                j+=1
                            child[k] = cc[i][j+1]
                            break
                if child[k]!=-1:
                    break
    return child

    
            

