def revNums(n):
    for i in range(n, -1, -1):
        yield i


n = int(input())
values = []

for i in revNums(n):
    values.append(str(i))

print(values)
