def SqrtNums(n):
    for i in range(n + 1):
        yield i*i


n = int(input())
values = []

for i in SqrtNums(n):
    values.append(str(i))

print(values)