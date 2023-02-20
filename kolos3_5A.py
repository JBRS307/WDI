from os import system


def is_magic(arr):
    leng = len(arr)
    m_sum = sum(arr[0])
    for i in range(1, leng):
        if sum(arr[i]) != m_sum:
            return False
    
    for j in range(leng):
        temp_sum = 0
        for i in range(leng):
            temp_sum += arr[i][j]
        if temp_sum != m_sum:
            return False
    
    return True
#-----------------------------------------------------

def magic(arr):
    leng = len(arr)
    def rec(arr, row, col, index, steps):
        nonlocal leng
        if steps == 0:
            return is_magic(arr)

        work_arr = [[0]*leng for _ in range(leng)]
        for i in range(leng):
            for j in range(leng):
                work_arr[i][j] = arr[i][j]
        
        if row:
            temp = work_arr[index][leng-1]
            for i in range(leng-1, 0, -1):
                work_arr[index][i] = work_arr[index][i-1]
            work_arr[index][0] = temp
            
            flag = False
            for i in range(leng):
                if rec(work_arr, True, False, i, steps-1) or rec(work_arr, False, True, i, steps-1):
                    flag = True
            return flag
        else:
            temp = work_arr[leng-1][index]
            for i in range(leng-1, 0, -1):
                work_arr[i][index] = work_arr[i-1][index]
            work_arr[0][index] = temp

            flag = False
            for i in range(leng):
                if rec(work_arr, True, False, i, steps-1) or rec(work_arr, False, True, i , steps-1):
                    flag = True
            return flag
    #-----------------------------------------------------

    flag = False
    for i in range(leng):
        if rec(arr, True, False, i, 2) or rec(arr, False, True, i, 2):
            flag = True
    
    return flag
#=====================================================

if __name__ == "__main__":
    system("clear")

    arr = [[3, 11, 14, 17],
           [6, 12, 7, 9],
           [10, 8, 16, 13],
           [5, 15, 4, 2]]
    
    print(magic(arr))