star = ["***", "* *", "***"]
starList = []

def fillStar(n: int):
    if n/3 == 1:
        starList.append(star)
    else:
        for i in range(n//3):
            if i != 5:
                starList.append(star)
    return starList

N = int(input())
fillStar(N)

count = 0
for i in starList:
    # print(i)
    for j in i:
        if count == 3:
            count = 0
            print(j, end='')
        else:
            count += 1
            print(j)

