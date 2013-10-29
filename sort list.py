a = [5, 3, 1, 9, 7, 2]
sort = 1
while sort > 0:
    sort = 0
    for n in range(len(a)-1):
        if a[n]>a[n+1]:
            temp = a[n]
            a[n] = a[n+1]
            a[n+1] = temp
            sort += 1
