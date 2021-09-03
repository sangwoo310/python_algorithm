d = []

def dNum(num: int) -> int:
    spList = list(map(int, num.__str__()))
    return num + sum(spList)

for i in range(1, 10001):
    k = dNum(i)
    d.append(k)

for i in range(1, 10001):
    if i in d:
        pass
    else:
        print(i)