s = input()
a = 0
b = 0
w = ('ауоыиэяюёе')
v = ('бвгджзйклмнпрстфхцчшщ')
for i in range(len(s)):
    if s[i] in w and s[i] in (w.upper()):
        a += 1
for k in range(len(s)):
    if s[k] in v and s[k] in (v.upper()):
        b += 1
print('Количество гласных букв равно', a)
print('Количество согласных букв равно', b)
