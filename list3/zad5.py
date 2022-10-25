#Wypisz 10 co do wielkości wartość w ciągu

if __name__ == "__main__":
    arr = [int(input())]
    while True:
        n = int(input())
        if n == 0:
            break
        for i in range(len(arr)):
            if n < arr[i]:
                arr.insert(i, n)
                break
        else:
            arr.append(n)
    
    print(arr[9])
