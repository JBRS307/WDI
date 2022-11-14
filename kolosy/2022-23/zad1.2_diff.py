#Znajdź taki kwadrat, żeby iloczyn jego narożników rozkładał się
#na dokładnie 2 czynniki pierwsze różne od siebie

#Rozwiązanie "Garek friendly spaghetti"

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
        if n%i == 0:
            count += 1
            if count > 2:
                return False
            while n%i == 0:
                n //= i
        i += 2
        
        if n%i == 0:
            count += 1
            if count > 2:
                return False
            while n%i == 0:
                n //= i
        i += 4
    
    return count == 2
#-----------------------------------------------------

def find_square(arr):
    leng = len(arr)

    size = 2
    while size <= leng-1:
        addition = size-1
        i = 0
        while i < leng-addition:
            j = 0
            while j < leng-addition:
                a = arr[i][j]
                b = arr[i][j+addition]
                c = arr[i+addition][j+addition]
                d = arr[i+addition][j]
                ones = [False]*4
                count_1 = 0
                for index, letter in enumerate((a, b, c, d)):
                    if letter == 1:
                        ones[index] = True
                        count_1 += 1
                
                if count_1 >= 2:
                    prod = 1
                    for index, letter in enumerate((a, b, c, d)):
                        if not ones[index]:
                            prod *= letter
                
                    if prime_factors_check(prod):
                        return size
                j += 1
            i += 1
        size += 1
    
    return 0
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [[randrange(1, k+1) for _ in range(n)] for _ in range(n)]

    print_arr(arr)

    print(find_square(arr))