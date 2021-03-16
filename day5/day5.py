with open('day5input.txt', 'r') as f:
    bp = f.read().split('\n')


def getid(partlist):
    seat_id = []
    for i in partlist:
        seat_row = 0
        max_row = 127
        seat_col = 0
        max_col = 7
        for j in i:
            if j == 'F':
                max_row -= (max_row - seat_row) // 2 + 1
            elif j == 'B':
                seat_row += (max_row - seat_row) // 2 + 1
            if j == 'L':
                max_col -= (max_col - seat_col) // 2 + 1
            elif j == 'R':
                seat_col += (max_col - seat_col) // 2 + 1

        seat_id.append(seat_row * 8 + seat_col)

    return seat_id


def find_missing(bplist):
    for i in range(len(bplist)):
        if abs(bplist[i] - bplist[i+1]) > 1:
            return bplist[i] + 1


print(getid(bp))
print(sorted(getid(bp)))
print(find_missing(sorted(getid(bp))))
