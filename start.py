import random

def rand_pop(N):
    numbers = []
    way = []
    for i in range(N):
        numbers.append(i)
    start = random.choice(numbers)
    way.append(start)
    numbers.remove(start)
    prev = start
    for i in range(N-1):
        next = random.choice(numbers)
        way.append(next)
        numbers.remove(next)
        prev = next
    return way

def nearest_neighbour(Arr, N):
    CurrentCity = -1
    TravOrder = []
    PathLen = 0
    for i in range(1,N):
        MinDist = 10000
        MinCity = -1
        if CurrentCity == -1:
            CurrentCity = random.randint(0,N-1)
            TravOrder.append(CurrentCity)
        for j in range(N):
            if (Arr[CurrentCity][j] != 0) and (Arr[CurrentCity][j] < MinDist) and (j not in TravOrder):
                MinCity = j
                MinDist = Arr[CurrentCity][j]
        CurrentCity = MinCity
        PathLen += MinDist
        
        TravOrder.append(MinCity)
    return TravOrder

def nearest_city(Arr, N):
    def NearestCity(Number,N):
        MinDist = 100
        MinCity = -1
        for j in range(N):
            if (Arr[Number][j] != 0) and (Arr[Number][j] < MinDist) and (j not in TravOrder):
                MinCity = j
                MinDist = Arr[CurrentCity][j]
        return(MinCity)
        
    TravOrder = [-1 for i in range(N)]
    CurrentCity = random.randint(0,N-1)
    TravOrder[0] = CurrentCity
    CityCount = 1
    LastCity = 0
    NewCity = 0
    for i in range(1,N):
        min = 1000
        for j in range(i):
            AsptNumber = NearestCity(TravOrder[j], N)
            if Arr[AsptNumber][TravOrder[j]]< min:
                LastCity = j
                min = Arr[AsptNumber][TravOrder[j]]
                NewCity = AsptNumber
        if LastCity + 1 == CityCount:
            TravOrder[CityCount] = NewCity
        else:
            for k in range(CityCount - 1, LastCity, -1):
                TravOrder[k+1] = TravOrder[k]
                TravOrder[k] = NewCity
        
        CityCount += 1
    return TravOrder