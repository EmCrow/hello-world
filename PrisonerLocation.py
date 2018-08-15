def ans(x,y):
    y2 = 0
    x2 = (y**2 + y) / 2 +1
    for z in range(y+2,x+y+1):
        x2 += z
    return int(x2 + y2)


def Curse(x,y,z,d):
    if x in d:
        return d[x]
        print(x)
        return Curse(x - 1, y, z + 1,d) + z
    else:
        print(x)
        ans = Curse(x -1, y, z + 1, d) + z
        d[x] = ans
        return ans

print(ans(5,9))
