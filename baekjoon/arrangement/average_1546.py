inputCount = int(input())
inputValue = list(map(int, input().split()))

total = 0

for i in inputValue:
    total += i / max(inputValue) * 100

print(total/inputCount)