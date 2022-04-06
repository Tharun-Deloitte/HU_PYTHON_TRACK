input = int(input('Input number of rows: '))

a = 0
rows = []
while a < input:
    l = 11 ** a
    k=len(str(l))
    for p in range(input-k):
        l=l*10
    rows.append(l)
    a += 1
for i in range(0,len(rows)):
    rows[i] = str(rows[i])
    print(rows[i])