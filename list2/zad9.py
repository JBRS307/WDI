#Obliczenie pola pod wykresem y = 1/x metodą prostokątów

def surface(n, k): #n - ile prostokątów, k - górna część zakresu
    s = 0
    d = (k-1)/n
    x = 1+d
    while x <= k:
        s += d * (1/x)
        x += d

    return s
#=====================================================
if __name__ == "__main__":
    k = int(input("Podaj gorna czesc zakresu: "))
    n = int(input("Podaj liczbe prostokatow: "))
    print(surface(n, k))
