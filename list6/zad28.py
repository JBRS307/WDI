from os import system
# from random import randrange


def count_ones(n):
    res = 0
    while n != 0:
        res += n%2
        n //= 2
    
    return res
#-----------------------------------------------------

def check_subsets(arr, set1=0, set2=0, set3=0, i=0):
    if i >= len(arr):
        return set1 == set2 and set2 == set3
    
    ones = count_ones(arr[i])
    return check_subsets(arr, set1+ones, set3, set3, i+1) or \
           check_subsets(arr, set1, set2+ones, set3, i+1) or \
           check_subsets(arr, set1, set2, set3+ones, i+1)
#=====================================================

if __name__ == "__main__":
    system("clear")

    # n, k = map(int, input("Rozmiar, zakres: ").strip().split())
    # system("clear")

    # arr = [randrange(1, k+1) for _ in range(n)]

    print(check_subsets([3, 3, 3]))
    print(check_subsets([2, 3, 5, 7, 15]))
    print(check_subsets([5, 7, 15]))
