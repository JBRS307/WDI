from os import system
from random import randrange


def print_arr(arr):
    for line in arr:
        for elem in line:
            print(elem, end='\t')
        print()
#=====================================================

def find_subset_rec(arr, target_sum, row=0, curr_sum=0, empty=True, columns=set()):
    if row >= len(arr):
        return target_sum == curr_sum and (not empty)
    
    for col in range(len(arr[row])):
        if col not in columns:
            if find_subset_rec(arr, target_sum, row+1, curr_sum, empty, {*columns}) or \
               find_subset_rec(arr, target_sum, row+1, curr_sum+arr[row][col], False, {*columns, col}):
                return True
                    
    return False
#=====================================================

if __name__ == "__main__":
    system("clear")

    k = int(input())
    system("clear")
    arr = [[randrange(1, k+1) for _ in range(8)] for _ in range(8)]
    print_arr(arr)
    summ = int(input('\n'))

    print(find_subset_rec(arr, summ))