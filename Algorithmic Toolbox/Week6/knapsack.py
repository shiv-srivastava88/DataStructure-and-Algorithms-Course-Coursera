m, n = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
res = []
for i in range(n+1):
    temp = []
    for j in range(m+1):
        temp.append(0)
    res.append(temp)
    
for i in range(1, n+1):
    for j in range(1, m+1):
        if l[i-1] > j:
            res[i][j] = res[i-1][j]
        else:
            res[i][j] = max((l[i-1] + res[i-1][j-l[i-1]]), res[i-1][j])


print(res[n][m])