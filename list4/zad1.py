#Wypełnienie tablicy dwuwymiarowej kolejnymi liczbami
#naturalnymi po spirali

def fill(n):
    arr = [[0]*n for _ in range(n)]

    steps = ((0, 1), (1, 0), (0, -1), (-1, 0))

    num = 1
    row = col = 0
    n -= 1
    while n > 0:
        for step in steps:
            for _ in range(n):
                arr[row][col] = num
                row += step[0]
                col+= step[1]
                num += 1
        
        n -= 2
        row += 1
        col += 1
    
    if n == 0:
        arr[row][col] = num

    return arr
#-----------------------------------------------------

def print_arr(arr):
    for line in arr:
        print(line)
#=====================================================

if __name__ == "__main__":
    n = int(input("Rozmiar: "))

    print_arr(fill(n))
