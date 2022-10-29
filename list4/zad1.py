#Wypełnienie tablicy dwuwymiarowej kolejnymi liczbami
#naturalnymi po spirali

def fill(n):
    arr = [[0 for i in range(n)] for j in range(n)]

    steps = ((0, 1), (1, 0), (0, -1), (-1, 0))

    num = 1
    ver = hor = 0
    n -= 1
    while n > 0:
        for step in steps:
            s_ver, s_hor = step
            for i in range(n):
                arr[ver][hor] = num
                ver += s_ver
                hor += s_hor
                num += 1
        
        n -= 2
        ver += 1
        hor += 1
    
    if n == 0:
        arr[ver][hor] = num

    return arr
#-----------------------------------------------------

def print_arr(arr):
    for line in arr:
        print(line)
#=====================================================

if __name__ == "__main__":
    n = int(input("Rozmiar: "))

    print_arr(fill(n))
