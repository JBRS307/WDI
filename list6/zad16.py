from os import system


def words_rec(word, vowels, v1, summ1, v2=0, summ2=0, i=0, res='', take=True):
    if i >= len(word):
        return summ1 == summ2 and v1 == v2, res
    if not take:
        return words_rec(word, vowels, v1, summ1, v2, summ2, i+1, res, True) or words_rec(word, vowels, v1, summ1, v2, summ2, i+1, res, False)

    res += word[i]
    if word[i] in vowels:
        v2 += 1
    if v2 > v1:
        return False, res
    
    summ2 += ord(word[i])
    if summ2 > summ1:
        return False, res
    
    return words_rec(word, vowels, v1, summ1, v2, summ2, i+1, res, True) or words_rec(word, vowels, v1, summ1, v2, summ2, i+1, res, False)
#-----------------------------------------------------

def words(word1, word2):
    vowels = "aeiouy"
    vowels_w1 = 0
    summ = 0
    for letter in word1:
        if letter in vowels:
            vowels_w1 += 1
        
        summ += ord(letter)
    
    return words_rec(word2, vowels, vowels_w1, summ)
#=====================================================

if __name__ == "__main__":
    system("clear")
    word1, word2 = input().strip().split()

    print(words(word1, word2))