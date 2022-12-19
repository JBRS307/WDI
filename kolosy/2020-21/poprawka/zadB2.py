from os import system


pieces = 0
#=====================================================

def cut_rec(word, leng, vowels, start=0, parts=0):
    global pieces
    if start >= leng:
        if parts >= 2:
            pieces += 1
        return

    for end in range(start, leng):
        for i in range(start, end+1):
            if word[i] in vowels:
                cut_rec(word, leng, vowels, end+1, parts+1)
                break
#-----------------------------------------------------

def cut(word):
    global pieces
    leng = len(word)
    
    cut_rec(word, leng, ['a', 'e', 'i', 'o', 'u', 'y'])
    res = pieces
    pieces = 0
    return res
#=====================================================

if __name__ == "__main__":
    system("clear")

    print(cut("student"))
    print(cut("sesja"))
    print(cut("ocena"))