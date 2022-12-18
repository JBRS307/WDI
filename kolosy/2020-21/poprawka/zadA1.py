from os import system


def lcm(a, b):
    x = a
    y = b

    while x != y:
        while x < y:
            x += a
        while y < x:
            y += b
    
    return x
#-----------------------------------------------------

def extend(arr):
    leng = len(arr)
    numerators = [arr[i][0] for i in range(leng)]
    denominators = [arr[i][1] for i in range(leng)]

    common = lcm(denominators[0], denominators[1])
    for i in range(2, leng):
        common = lcm(common, denominators[i])
    
    for i in range(leng):
        quot = common//denominators[i]
        numerators[i] *= quot
        denominators[i] = common
    
    return [(numerators[i], denominators[i]) for i in range(leng)]
#-----------------------------------------------------

def longest(arr):
    leng = len(arr)

    arr = extend(arr)
    
    quot = [None, None]
    for i in range(1, leng):
        if arr[i-1][0] != 0:
            quot[0] = arr[i][0]/arr[i-1][0]
            quot[1] = arr[i][1]/arr[i-1][1]
            curr = i
            break
    
    if quot is [None, None]:
        if arr[leng-1][0] == 0:
            return leng
        else:
            return leng-1
    
    str_leng = 1
    max_leng = 1
    while curr < leng:
        if quot[0] == 0 and arr[curr][0] == 0:
            str_leng += 1
            curr += 1
        elif arr[curr-1][0] * quot[0] == arr[curr][0] and arr[curr-1][1] * quot[1] == arr[curr][1]:
            str_leng += 1
            curr += 1
        else:
            max_leng = max(max_leng, str_leng)
            str_leng = 1
            for i in range(curr, leng):
                if arr[curr-1][0] != 0:
                    quot[0] = arr[i][0]/arr[i-1][0]
                    quot[1] = arr[i][1]/arr[i-1][1]
                    curr = i
                    break
    
    max_leng = max(max_leng, str_leng)

    return max_leng if max_leng > 2 else 0
#=====================================================

if __name__ == "__main__":
    system("clear")

    print(longest( [(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)])) # wypisze 4
    print(longest( [(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)] )) # wypisze 3
    print(longest( [(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)])) # wypisze 6
    print(longest( [(1,2),(2,3),(3,4),(4,5),(5,6)] )) # wypisze 0

    # print(shorten((0, 6)))
