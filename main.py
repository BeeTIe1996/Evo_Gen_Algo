from operators import printMatrix, getWayLenght
import crossover
import mutation
import parent_pair
import selection
import start

if __name__ == '__main__':
    TaskSize = 15

    wayMatrix = [[] for i in range(TaskSize)]

    with open('data.txt') as file:
        for i in range(TaskSize):
            wayMatrix[i] = [float(x) for x in file.readline().split()]

    printMatrix(wayMatrix)

    solution = []
    for i in range(TaskSize):
        solution.append(0)

    print("Start working...")
    print("Count of person?")
    num_pop = int(input())
    print("Start population: 0 - random, 1 - nearby city, 2 - nearby neighbour")
    ch1 = int(input())
    print("Choice of parents: 0 - panmix, 1 - negative associative cross")
    ch2 = int(input())
    print("Crossover: 0 - Order, 1 - Partition")
    ch3 = int(input())
    print("Mutation: 0 - Point, 1 - Saltation")
    ch4 = int(input())
    print("Selection: 0 - B-tournament, 1 - Proportional")
    ch5 = int(input())
    print("Amount of generation?")
    num_gen = int(input())

    pop_new = []
    way_new = []
    index_chosen = []

    np = []
    total_way=[]
    best_solution = []
    best_way = []
    min_it = -1
    print("Start population:")
    
    min_way = 10000
    for i in range(num_pop):
        if ch1 == 0:
            np.append(start.rand_pop(TaskSize))
        elif ch1 == 1:
            np.append(start.nearest_city(wayMatrix, TaskSize))
        elif ch1 == 2:
            np.append(start.nearest_neighbour(wayMatrix, TaskSize))
        total_way.append(getWayLenght(np[i], wayMatrix))
        if min_way > total_way[i]:
            min_way = total_way[i]
            min_it = i
    print(np)
    print(total_way)
    best_solution.append(np[min_it])
    best_way.append(total_way[min_it])
    print(best_solution)
    print(best_way)

    num_of_cur_gen = 1

    while num_of_cur_gen <= num_gen:
        print("Generation -", num_of_cur_gen)

        rp = []
        for j in range(num_pop):
            rp.append(0)

        cr = []
        for j in range(num_pop):
            cr.append(0)
        
        for i in range(num_pop):
            if ch2 == 0:
                rp[i] = parent_pair.panmix(np)
            elif ch2 == 1:
                rp[i] = parent_pair.negative_acc(np)
        
        for i in range(num_pop):
            if ch3 == 0:
                cr[i] = crossover.ord_cross(rp[i][0],rp[i][1], TaskSize)
            elif ch3 == 1:
                cr[i] = crossover.part_cross(rp[i][0],rp[i][1], TaskSize)
        
        for i in range(len(cr)):
            pop_new.append(cr[i])
    
        if ch4 == 0:
            pop_new, index = mutation.point_mut(pop_new, TaskSize)
        elif ch4 == 0:
            pop_new, index = mutation.saltation(pop_new, TaskSize)
        
        for i in range(len(pop_new)):
            way_new.append(getWayLenght(pop_new[i],wayMatrix))
        
        for i in range(len(pop_new)):
            if way_new[i] < min_way:
                min_way = way_new
                min_it = i
        if ch5 == 0:
            index_chosen = selection.b_tour(pop_new, way_new, num_pop)
        elif ch5 == 1:
            prob_arr = selection.proportional(way_new)
            index_chosen = selection.copy_roulette(prob_arr, num_pop)
        temp = []
        for i in range(len(index_chosen)):
            temp.append(pop_new[index_chosen[i]])
        
        pop_new = temp

        way_new = []

        for i in range(len(pop_new)):
            way_new.append(getWayLenght(pop_new[i],wayMatrix))
        print("Final Pop in Gen", num_of_cur_gen)
        for i in range(len(pop_new)):
            print(pop_new[i],'\t', way_new[i])
            if min_way > way_new[i]:
                min_way = way_new[i]
                min_it = i
        print("Best person:", '\t', pop_new[min_it], '\t', "Way:",'\t', min_way)
        best_solution.append(pop_new[min_it])
        best_way.append(min_way)

        num_of_cur_gen += 1

        np = pop_new.copy()
        pop_new.clear()
        rp.clear()
        cr.clear()

    
    print("Best Solution:")
    print("Person:",'\t', best_solution[-1], '\t', "Way:", '\t', best_way[-1])