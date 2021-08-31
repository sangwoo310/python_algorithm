value = int(input()) * int(input()) * int(input())

valueList = list(map(int, str(value)))

for i in range(10):
    print(valueList.count(i))

