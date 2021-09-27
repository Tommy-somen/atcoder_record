n,s,d = list(map(int,input().split()))
xy = [list(map(int,input().split())) for _ in range(n)]

cnt = 0

for i in xy:
    if i[0] < s and i[1] > d:
        cnt += 1

if cnt > 0:
    print("Yes")
else:
    print("No")
