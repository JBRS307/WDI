#y jest traktowana jako samogłoska

from os import system


pieces = 0
#=====================================================

def cut_rec(word, leng, vowels, start=0):
    global pieces
    if start >= leng:
        pieces += 1
        return

    for end in range(start, leng):
        vow_count = 0
        for i in range(start, end+1):
            if word[i] in vowels:
                vow_count += 1
        if vow_count >= 2:
            break
        if vow_count == 1:
            cut_rec(word, leng, vowels, end+1)
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
    print(cut("informatyka"))