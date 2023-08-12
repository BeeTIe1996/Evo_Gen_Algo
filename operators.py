def getWayLenght(Arr, matrix):
    wayLenght = 0
    for i in range(len(Arr)):
        if i == len(Arr)-1:
            wayLenght += matrix[Arr[i]][Arr[0]]
        else:
            wayLenght += matrix[Arr[i]][Arr[i+1]]
    return wayLenght


def printMatrix (matrix): 
    for row in matrix: 
        for x in row: 
            print ( "{:.3f}".format(x), end = " " ) 
        print ()