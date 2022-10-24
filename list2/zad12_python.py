#A tak się to powinno zrobić w pythonie

def checkDigit(n):
    n = str(n)
    length = str(len(n))
    return True if length in n else False
#=====================================================
if __name__ == "__main__":
    n = int(input())
    print(checkDigit(n))