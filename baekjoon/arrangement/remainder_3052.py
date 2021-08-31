valueArr = []
count = 0

for i in range(10):
    valueArr.append(int(input()) % 42)

for i in range(42):
    if valueArr.count(i) > 0:
        count += 1

print(count)
