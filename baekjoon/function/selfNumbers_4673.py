# d = []
#
# def dNum(num: int) -> int:
#     spList = list(map(int, num.__str__()))
#     return num + sum(spList)
#
# baseNum = 1
# while baseNum < 100:
#     baseNum = dNum(baseNum)
#     # print(baseNum)
#     d.append(baseNum)
#     dNum(baseNum)
#
# print(d)

# for i in range(100):
#     baseNum = dNum(i+1)
#     # print(baseNum)
#     if baseNum <= 10000 and d.count(baseNum) == 0:
#         d.append(i)
#
# print(d)
# print(dNum(1))

for i in range(1, 100):
    for j in str(i):
        i += int(j)
    print(i)