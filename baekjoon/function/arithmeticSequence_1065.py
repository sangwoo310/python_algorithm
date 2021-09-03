def arithmetic(n: int) -> bool:
    resultBool = False

    if n < 100:
        return True

    nList = list(str(n))
    difNum = int(nList[0]) - int(nList[1])

    for i in range(1, len(nList)-1):
        if difNum != int(nList[i]) - int(nList[i+1]):
            resultBool = False
            break
        else:
            difNum = int(nList[i]) - int(nList[i+1])
            resultBool = True

    return resultBool

count = 0
for i in range(1, int(input()) + 1):
    if arithmetic(i):
        # print(i)
        count += 1

print(count)
