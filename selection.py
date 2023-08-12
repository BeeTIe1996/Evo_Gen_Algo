import numpy as np
import random

def proportional(way_arr):
    sum = sum(way_arr)
    prob_arr = []
    for desc in way_arr:
        prob_arr.append(desc/sum)
    return prob_arr

def copy_roulette(prob_arr, amount):
    index_chosen = np.random.choice(len(prob_arr), amount, p=prob_arr, replace=False)
    return index_chosen

def b_tour(arr, way_arr, amount):
    index_chosen = []
    b = 5
    for i in range(amount):
        B = []
        B = random.sample(arr,b)
        min_index = 0
        min = 10000
        for j in range(b):
            if way_arr[arr.index(B[j])]<min:
                min = way_arr[arr.index(B[j])]
                min_index = j
        index_chosen.append(arr.index(B[j]))
    return index_chosen
