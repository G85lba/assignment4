def SqrtNums(a, b):
    for i in range(a, b + 1):
        yield i*i


a = int(input())
b = int(input())
values = []

for i in SqrtNums(a, b):
    values.append(str(i))

print(values)