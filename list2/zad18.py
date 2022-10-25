#Wypisywanie między dwoma ciągami
#Nie mam pojęcia czy to jest dobrze, nie chce mi się sprawdzać.

if __name__ == "__main__":
    if int(input()) != 0:
        exit()
    print(2)
    if int(input()) != 1:
        exit()
    
    b = 2
    print(b)

    bMin1 = 2
    aMin1 = 1
    aMin2 = 0
    a = 1
    b = 4
    while True:
        n = int(input())
        if n == a:
            print(b)
            a, aMin1, aMin2, b, bMin1 = aMin1 - bMin1*aMin2, a, aMin1 , bMin1+2*aMin1, b
        else:
            exit()