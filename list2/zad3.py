#Sprawdź czy liczba jest palindromem w dziesiętnym i binarnym

def isPalindrome(n):
    if n == n[::-1]:
        return True
    return False
#-----------------------------------------------------
def checkNum(n):
    if isPalindrome(n):
        decPalindrome = "Tak"
    else:
        decPalindrome = "Nie"
    
    n = bin(int(n))[2:]
    if isPalindrome(n):
        binPalindrome = "Tak"
    else:
        binPalindrome = "Nie"
    
    return decPalindrome, binPalindrome
#=====================================================
if __name__ == "__main__":
    n = input().strip()

    decimal, binary = checkNum(n)
    print("Palindrom decymalny:", decimal)
    print("Palindrom binarny:", binary)