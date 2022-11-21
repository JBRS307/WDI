def find_subset(arr, i, index_sum = 0, elem_sum = 0, best_leng = float('inf'), leng=0):
    if i >= len(arr):
        return (index_sum == elem_sum and elem_sum > 0), elem_sum, leng
    
    best_sum = 0
    possible = False

    res, summ, new_leng = find_subset(arr, i+1, index_sum, elem_sum, best_leng, leng)
    if res and new_leng < best_leng:
        best_leng = new_leng
        best_sum = summ
        possible = True
    
    res, summ, new_leng = find_subset(arr, i+1, index_sum+i, elem_sum+arr[i], best_leng, leng+1)
    if res and new_leng < best_leng:
        best_leng = new_leng
        best_sum = summ
        possible = True
    
    return possible, best_sum, best_leng
#=====================================================\
if __name__ == "__main__":
    arr = [1,7,3,5,11,2]
    # arr = [22, 56, 21, 23, 67]

    print(find_subset(arr, 0))