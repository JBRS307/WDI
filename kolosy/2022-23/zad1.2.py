#Znajdź taki kwadrat, żeby iloczyn jego narożników rozkładał się
#na dokładnie 2 czynniki pierwsze różne od siebie

from random import randrange


def print_arr(arr):
    for line in arr:
        print(line)
#-----------------------------------------------------

def prime_factors_check(n):
    count = 0
    if not n%2:
        count += 1
        while not n%2:
            n //= 2
    
    if not n%3:
        count += 1
        while not n%3:
            n //= 3
    
    i = 5
    while n != 1:
        if not n%i:
            count += 1
            if count > 2:
                return False
            while not n%i:
                n //= i
        i += 1
    
    return True if count == 2 else False
#-----------------------------------------------------

def find_square(arr, leng):
    n = 0
    min_square = [(None, None), float('inf')] #Współrzędne punktu A i rozmiar kwadratu
    while n < leng:
        for i in range(leng-n):
            a = arr[i][n]
            for j in range(1, min(leng-n, leng-i)):
                b = arr[i][n+j]
                c = arr[i+j][n+j]
                d = arr[i+j][n]
                prod = a*b*c*d
                if prime_factors_check(prod):
                    if j+1 < min_square[1]:
                        min_square[1] = j+1
                        min_square[0] = (i, n)
                    break #Nie ma sensu szukać dalej, te kwadraty będą tylko większe
        n += 1
    
    return min_square if min_square != [(None, None), float('inf')] else None
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [[randrange(1, k+1) for _ in range(n)] for _ in range(n)]

    print_arr(arr)

    print(find_square(arr, n))