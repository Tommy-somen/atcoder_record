n = int(input())
sunuke = [list(map(int,input().split())) for _ in range(n)]
p = []

for i in sunuke:
    if (i[2] - i[0]) > 0:
        p.append(i[1])

if len(p) > 0:
    print(min(p))
else:
    print(-1)
