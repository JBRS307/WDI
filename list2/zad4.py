#Zlicz liczby 2,3,5 w przedziale 1-n. Liczba 2, 3, 5 to liczba, która w
#rozkładzie na czynniki pierwsze nie posiada innych czynników niż 2,3, 5

def count_2_3_5(n):
    counter = 0

    n2 = 1
    while n2 <= n:
        n3 = n2
        while n3 <= n:
            n5 = n2
            while n5 <= n:
                counter += 1
                n5 *= 5
            n3 *= 3
        n2 *= 2
    
    return counter
#=====================================================
if __name__ == "__main__":
    n = int(input())
    print(count_2_3_5(n))