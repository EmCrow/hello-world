
def Coordinates(start, end):
    y1 = int(start) // 8
    x1 = int(start) % 8

    y2 = int(end) // 8
    x2 = int(end)% 8
    return x1, y1, x2, y2

def CheckCorner(x1,y1,x2,y2):
    a = [0,7]
    if (x1 in a and y1 in a) or (x2 in a and y2 in a):
        return True
    return False

def DiffCheck(a):
    count = 0
    b = a
    Z = KnownPairs()
    b.sort()
    while b[0] >= 0 and b[1] >= 0 and b not in Z:
        if b[0] % 2 == 0 and b[1] % 2 != 0 and b[0] != 0:
            b[0] = b[0] - 2
            b[1] = b[1] - 1
        else:
            b[0] = b[0] - 1
            b[1] = b[1] - 2
        b[0] = abs(b[0])
        b[1] = abs(b[1])
        count += 1
        b.sort()
    if b in Z:
        count += KnownPairConditionals(b)
    return count


def KnownPairConditionals(diff):
    count = 0
    if diff == [1,2]:
        count+=1
    if diff == [0,1] \
           or diff == [0,3] \
           or diff == [2,3]:
        count+=3
    if diff == [0,2] or diff == [1,1] or diff == [1,3]:
        count+=2
    return count


def KnownPairs():
    knownDiffPairs =[[0,0],[0,1],[0,2],[0,3],[1,1],[1,2],[1,3],[2,3]]
    return knownDiffPairs

def answer(start, end):
    count = 0
    x1, y1, x2, y2 = Coordinates(start, end)
    knownDiffPairs = KnownPairs()
    cornerCheck = CheckCorner(x1,y1,x2,y2)

    diff_X = x1 - x2
    diff_Y = y1 - y2

    diff = ([abs(diff_X), abs(diff_Y)])

    while True:
        diff.sort()
        if diff in knownDiffPairs:
            if diff == [1,1] and cornerCheck:
                count+=4
                return count
            else:
                return KnownPairConditionals(diff)
            return count
        else:
            return DiffCheck(diff)
