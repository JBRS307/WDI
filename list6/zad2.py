#”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
#waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
#naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
#równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool

#Chodzi o to, że suma wag w każdym podzbiorze ma być jednakowa

from os import system


def prime_factors(n):
    counter = 0
    if n%2 == 0:
        counter += 1
        while n%2 == 0:
            n //= 2
        
    if n%3 == 0:
        counter += 1
        while n%3 == 0:
            n //= 3
    
    i = 5
    while n != 1:
        if n%i == 0:
            counter += 1
            while n%i == 0:
                n //= i
        i += 2
        
        if n%i == 0:
            counter += 1
            while n%i == 0:
                n //= i
        i += 4

    return counter
#=====================================================

def change_arr(arr):
    for i in range(len(arr)):
        arr[i] = prime_factors(arr[i])
    return arr
#-----------------------------------------------------

def find_sets_rec(arr, set1=0, set2=3, set3=0, i=0):
    if i >= len(arr):
        return set1 == set2 and set2 == set3
    return find_sets_rec(arr, set1+arr[i], set2, set3, i+1) or \
           find_sets_rec(arr, set1, set2+arr[i], set3, i+1) or \
           find_sets_rec(arr, set1, set2, set3+arr[i], i+1)
#-----------------------------------------------------

def find_sets(arr):
    arr = change_arr(arr)
    if sum(arr)%3 == 0:
        return find_sets_rec(arr)
    
    return False
#=====================================================

if __name__ == "__main__":
    system("clear")

    arr = [1, 2, 6, 30, 64]
    print(find_sets(arr))


