from os import system


def check_subsets(arr, k, sum1=0, sum2=0, set1=0, set2=0, i=0):
    if i >= len(arr):
        return sum1 == sum2 and set1 == k and set2 == k
    
    return check_subsets(arr, k, sum1+arr[i], sum2, set1+1, set2, i+1) or \
           check_subsets(arr, k, sum1, sum2+arr[i], set1, set2+1, i+1) or \
           check_subsets(arr, k, sum1, sum2, set1, set2, i+1)
#=====================================================

if __name__ == "__main__":
    system("clear")

    arr = [1, 2, 3, 1, 2, 3, 7]
    k = int(input())

    print(check_subsets(arr, k))