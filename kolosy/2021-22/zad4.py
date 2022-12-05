from os import system


fib = [1, 1]
#=====================================================

def extend_fib(num):
    global fib
    while fib[-1] < num:
        fib.append(fib[-1]+fib[-2])
#-----------------------------------------------------

def find_subseq(arr):
    global fib
    leng = len(arr)
    
    for row in range(leng):
        for i in range(2, leng):
            if arr[row][i] == arr[row][i-1] + arr[row][i-2]:
                if arr[row][i] > fib[-1]:
                    extend_fib(arr[row][i])
                if arr[row][i] in fib:
                    return (row, i, arr[row][i]+arr[row][i-1]+arr[row][i-2])
        
        for i in range(-3, -(leng+1), -1):
            if arr[row][i] == arr[row][i+1] + arr[row][i+2]:
                if arr[row][i] > fib[-1]:
                    extend_fib(arr[row][i])
                if arr[row][i] in fib:
                    return (row, leng+i, arr[row][i] + arr[row][i+1] + arr[row][i+2])
    
    
    for col in range(leng):
        for i in range(2, leng):
            if arr[i][col] == arr[i-1][col] + arr[i-2][col]:
                if arr[i][col] > fib[-1]:
                    extend_fib(arr[i][col])
                if arr[i][col] in fib:
                    return (i, col, arr[i][col] + arr[i-1][col] + arr[i-2][col])
        
        for i in range(-3, -(leng+1), -1):
            if arr[col][i] == arr[col][i+1] + arr[col][i+2]:
                if arr[col][i] > fib[-1]:
                    extend_fib(arr[col][i])
                if arr[i][col] in fib:
                    return (leng+1, col, arr[i][col] + arr[i-1][col] + arr[i-2][col])
#=====================================================

if __name__ == "__main__":
    system("clear")

    arr = [[5, 3, 2, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]
    
    print(*find_subseq(arr))