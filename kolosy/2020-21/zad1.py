def multi(arr):
    longest = 0
    for word in arr:
        leng = len(word)
        
        if leng < 2:
            continue

        div = leng-1

        while div > 0:
            if leng%div == 0:
                flag = True
                for i in range(leng):
                    if word[i] != word[i%div]:
                        flag = False
                        break
                if flag:
                    break
            div-=1

        if flag:
            longest = max(longest, leng)
    
    return longest
#=====================================================

if __name__ == "__main__":
    arr = ["abaabaabaaba", "gfsdiuhdsf", "aaaaaaaaa", "fjooauufvhchdffh", "abcdabcdabcdabcdabcd", "dsskdjfjjejd",
           "ababababababababa", "abababababababab", "abababababababac"]
    
    print(len(arr[4]))
    print(multi(arr))