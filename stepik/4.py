s = int(input())
b = ''
while s > 0:
    b = str(s % 2) + b
    s //= 2
print(b)