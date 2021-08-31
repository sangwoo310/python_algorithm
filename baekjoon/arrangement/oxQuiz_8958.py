result = []

for i in range(int(input())):
    total = 0
    accumulate = 0

    value = list(input())
    for k in value:
        if k == "O":
            accumulate += 1
            total += accumulate
        else:
            accumulate = 0
    result.append(total)

for i in result:
    print(i)

