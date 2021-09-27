from collections import deque

R,C = list(map(int,input().split()))
sy,sx = list(map(int,input().split()))
gy,gx = list(map(int,input().split()))

S = []
for i in range(R):
  s = input()
  S.append(s)

sy -= 1
sx -= 1
gy -= 1
gx -= 1

distance = []
for j in range(R):
  distance.append([-1]*C)
  
Q = deque()
Q.append([sy,sx])
distance[sy][sx] = 0

while len(Q) > 0:
  py,px = Q.popleft()
  for py2,px2 in [[py+1,px],[py-1,px],[py,px+1],[py,px-1]]:
    if not (0 <= py2 < R) and (0 <= px2 < C):
      continue
    if S[py2][px2] == "#":
      continue
    if distance[py2][px2] == -1:
      distance[py2][px2] = distance[py][px] + 1
      Q.append([py2,px2])

print(distance[gy][gx])
