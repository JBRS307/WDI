from os import system
from math import sqrt
from random import uniform
# from random import randrange


points = []
#=====================================================

def print_arr(arr):
    for line in arr:
        print(line)
#=====================================================

def rec_avg(arr, take, i=0, curr_sum = [0, 0, 0], elems = 0):
    global points
    
    if i >= len(arr):
        if elems >= 3:
            points.append([curr_sum[0]/elems, curr_sum[1]/elems, curr_sum[2]/elems])
        return
    
    if take:
        curr_sum[0] += arr[i][0]
        curr_sum[1] += arr[i][1]
        curr_sum[2] += arr[i][2]
        elems += 1
    
    rec_avg(arr, True, i+1, curr_sum, elems)
    rec_avg(arr, False, i+1, curr_sum, elems)
#-----------------------------------------------------

def find_avg(arr, r):
    global points
    
    rec_avg(arr, True)
    rec_avg(arr, False)
    
    for elem in points:
        if sqrt(elem[0]**2 + elem[1]**2 + elem[2]**2) <= r:
            return True
    return False
#=====================================================

if __name__ == "__main__":
    system("clear")

    n, k = map(int, input().strip().split())

    arr = [(uniform(-k, k+1), uniform(-k, k+1), uniform(-k, k+1)) for _ in range(n)]

    r = int(input())
    system("clear")
    
    print_arr(arr)
    print(find_avg(arr, r))