n, m = 3, 4
arr = [[0]*m for _ in range(n)]
index = 1
for i in range(n):
    for j in range(m):
        arr[i][j] = index
        index += 1
print("now")
for a in arr:
    print(a)


# 90 rotate
new = [[0]*n for _ in range(m)]
for i in range(n):
    for j in range(m):
        new[j][n-1-i] = arr[i][j]
print("90")
for a in new:
    print(a)


# 180 rotate
new = [[0]*m for _ in range(n)]
# new = [[0]*n for _ in range(m)]
for i in range(n):
    for j in range(m):
        new[n-1-i][m-1-j] = arr[i][j]
print("180")
for a in new:
    print(a)


# 270 -90 rotate
new = [[0]*n for _ in range(m)]
for i in range(n):
    for j in range(m):
        new[m-1-j][i] = arr[i][j]
print("180")
for a in new:
    print(a)