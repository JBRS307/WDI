def queen(queens):
    cols = [False]*100
    rows = [False]*100

    #Przekątne, jest ich 2n-1
    dia1 = [False]*199 #od lewej w prawo w dół
    dia2 = [False]*199 #od prawej w lewo w dół

    for x, y in queens: #Test dla rzędów i kolumn
        if rows[x] or cols[y]:
            return False
        
        rows[x] = True
        cols[y] = True

        if dia1[99+y-x] or dia2[x+y]: #Każda przekątna ma swój numer równy sumie współrzędnych, które na niej leżą
            return False
        
        dia1[99+y-x] = True
        dia2[x+y] = True
    
    return True
#=====================================================


