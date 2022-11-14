def distance(arr):
    leng = len(arr)
    smallest = [1] * leng
    greatest = [0] * leng
    pos_smallest = 0
    pos_greatest = 0

    for pos, row in enumerate(arr):
        i = 0
        while i < leng and row[i] == smallest[i]:
            i += 1
        
        if i < leng and row[i] == 0:
            smallest = row
            pos_smallest = pos
        
    for pos, row in enumerate(arr):
        i = 0
        while i < leng and row[i] == greatest[i]:
            i += 1
        
        if i < leng and row[i] == 1:
            greatest = row
            pos_greatest = pos
    
    return abs(pos_greatest-pos_smallest)
#=====================================================

if __name__ == "__main__":
    print(distance([
    [1,0,0,0,1,1,1,0],
    [1,0,1,0,1,1,1,0],
    [0,0,0,0,1,1,1,0],
    [0,0,0,0,1,0,1,0],
    [1,0,0,0,1,1,1,1],
    [1,1,0,1,1,0,1,0],
    [1,0,0,0,0,0,1,0],
    [1,1,1,0,1,1,1,1]
    ]))