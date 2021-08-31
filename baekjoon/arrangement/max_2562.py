inputValue = []
for i in range(9):
    inputValue.append(int(input()))

print(max(inputValue))
print(inputValue.index(max(inputValue))+1)
