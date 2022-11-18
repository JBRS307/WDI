#Kalkulator ułamków zwykłych
#Działa na wersji python 3.10+

def gcf(a, b):
    while b != 0:
        a, b = b, a%b
    
    return abs(a)
#-----------------------------------------------------

def shorten(num):
    div = gcf(num[0], num[1])
    return (num[0]//div, num[1]//div)
#-----------------------------------------------------

def addition(a, b):
    return ((a[0]*b[1])+(b[0]*a[1]), a[1]*b[1])
#-----------------------------------------------------

def subtraction(a, b):
    return ((a[0]*b[1])-(b[0]*a[1]), a[1]*b[1])
#-----------------------------------------------------

def multiplication(a, b):
    return (a[0]*b[0], a[1]*b[1])
#-----------------------------------------------------

def divide(a, b):
    return (a[0]*b[1], a[1]*b[0])
#-----------------------------------------------------

def print_num(num):
    print(f"= {num[0]}/{num[1]}")
#=====================================================

if __name__ == "__main__":
    a = tuple(map(int, input().strip().split()))
    b = tuple(map(int, input().strip().split()))

    if a[1] == 0 or b[1] == 0:
        raise ZeroDivisionError("Dzielisz przez 0")

    print_num(a)
    print_num(b)

    print('''\nPodaj numer operacji:
1. Dodawanie
2. Odejmowanie
3. Mnozenie
4. Dzielenie''')

    operation = input()

    match operation:
        case '1':
            print_num(shorten(addition(a, b)))
        case '2':
            print_num(shorten(subtraction(a, b)))
        case '3':
            print_num(shorten(multiplication(a, b)))
        case '4':
            print_num(shorten(divide(a, b)))
        case _:
            print_num(shorten(addition(a, b)))
            print_num(shorten(subtraction(a, b)))
            print_num(shorten(multiplication(a, b)))
            print_num(shorten(divide(a, b)))
