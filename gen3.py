def DivCheck(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
values = []

for i in DivCheck(n):
    values.append(str(i))

print(values)