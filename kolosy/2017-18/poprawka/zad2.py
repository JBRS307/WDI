from os import system


def pairs(arr1, arr2):
    leng = len(arr1)

    max_pairs = 0

    def rec(arr1, arr2, leng, i=0, sum1=0, sum2=0, leng1=0, leng2=0):
        if i == leng:
            if sum1 == sum2 and leng1 == leng2:
                nonlocal max_pairs
                max_pairs = max(max_pairs, leng1)
            return
        
        rec(arr1, arr2, leng, i+1, sum1, sum2, leng1, leng2)
        rec(arr1, arr2, leng, i+1, sum1+arr1[i], sum2, leng1+1, leng2)
        rec(arr1, arr2, leng, i+1, sum1, sum2+arr2[i], leng1, leng2+1)
        rec(arr1, arr2, leng, i+1, sum1+arr1[i], sum2+arr2[i], leng1+1, leng2+1)
    #-----------------------------------------------------

    rec(arr1, arr2, leng)
    return max_pairs
#=====================================================

if __name__ == "__main__":
    system("clear")

    arr1 = [1,1,2,3,1]
    arr2 = [2,1,1,1,1]

    print(pairs(arr1, arr2))