from random import uniform

def find_substr(arr):
    leng = len(arr)

    if leng < 2:
        raise ValueError("Za krotka tablica")

    quot = arr[1]/arr[0] if arr[0] != 0 else 1
    diff = arr[1] - arr[0]
    
    leng_a = 1
    leng_g = 1

    count_a = 0
    count_g = 0

    for i in range(1, leng):
        if arr[i] == arr[i-1] + diff:
            leng_a += 1
        else:
            if leng_a > 2:
                count_a += 1
            leng_a = 1
            diff = arr[i] - arr[i-1]

        if arr[i] == arr[i-1] * quot:
            leng_g += 1
        else:
            if leng_g > 2:
                count_g += 1
            leng_g = 1
            quot = arr[i]/arr[i-1] if arr[i-1] != 0 else 1

    if leng_a > leng_g:
        return 1
    elif leng_a < leng_g:
        return -1
    else:
        return 0
#=====================================================

if __name__ == "__main__":
    leng = int(input("Rozmiar tablicy: "))
    mini = float(input("Najmniejsza liczba: "))
    maxi = float(input("Najwieksza liczba: "))

    arr = [uniform(mini, maxi) for _ in range(leng)]

    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 4, 8, 4, 5, 6, 7]

    print(*arr)
    print(find_substr(arr))

