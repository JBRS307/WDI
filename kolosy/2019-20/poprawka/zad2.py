from os import system


class Brick:
    def __init__(self, a, b):
        self.a = a
        self.b = b
#=====================================================

def domino_rec(arr, leng, free_end, last, ignore, str_leng=1):
    max_leng = str_leng
    for i in range(leng):
        if i not in ignore:
            if free_end == 'a':
                if arr[last].a == arr[i].a:
                    temp_leng = domino_rec(arr, leng, 'b', i, [*ignore, i], str_leng+1)
                    max_leng = max(max_leng, temp_leng)
                if arr[last].a == arr[i].b:
                    temp_leng = domino_rec(arr, leng, 'a', i, [*ignore, i], str_leng+1)
                    max_leng = max(max_leng, temp_leng)
            elif free_end == 'b':
                if arr[last].b == arr[i].a:
                    temp_leng = domino_rec(arr, leng, 'b', i, [*ignore, i], str_leng+1)
                    max_leng = max(max_leng, temp_leng)
                if arr[last].b == arr[i].b:
                    temp_leng = domino_rec(arr, leng, 'a', i, [*ignore, i], str_leng+1)
                    max_leng = max(max_leng, temp_leng)

    return max_leng
#-----------------------------------------------------

def domino(arr):
    leng = len(arr)

    max_leng = 0
    for start in range(leng):
        res = max(domino_rec(arr, leng, 'a', start, [start]), domino_rec(arr, leng, 'b', start, [start]))
        max_leng = max(max_leng, res)
    
    return max_leng
#=====================================================
if __name__ == "__main__":
    system("clear")

    arr = []
    arr.append(Brick(2, 8))
    arr.append(Brick(0, 1))
    arr.append(Brick(2, 3))
    arr.append(Brick(3, 6))
    arr.append(Brick(2, 6))
    arr.append(Brick(2, 9))
    arr.append(Brick(3, 4))
    arr.append(Brick(6, 7))

    print(domino(arr))