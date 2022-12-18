from os import system


def check_field(knights, row, col, knight_row, knight_col, ver, hor):
    for i in range(8):
        if (row+ver[i] != knight_row and col+ver[i] != knight_col) and ((row+ver[i], col+hor[i]) in knights):
            return False
    return True
#-----------------------------------------------------

def remove_knight(knights, leng):
    max_safe = 0

    ver = (2, 1, -2, -1, 2, 1, -2, -1)
    hor = (1, 2, 1, 2, -1, -2, -1, -2)
    # knight_num = -1
    for knight in knights:
        # knight_num += 1
        safe = 0
        row = knight[0]
        col = knight[1]
        if check_field(knights, row, col, row, col, ver, hor):
                safe += 1

        for i in range(8):
            if (0 <= row+ver[i] < leng and 0 <= col+hor[i] < leng) and ((row+ver[i], col+hor[i]) not in knights):
                if check_field(knights, row+ver[i], col+hor[i], row, col, ver, hor):
                    safe += 1
        
        max_safe = max(safe, max_safe)
    
    return max_safe
#=====================================================

if __name__ == "__main__":
    system("clear")

    knights1 = [(1, 1), (2, 3), (4, 1), (4, 5)]
    knights2 = [(1, 0), (2, 3), (4, 1), (4, 5)]

    print(remove_knight(knights1, 6))
    print(remove_knight(knights2, 8))