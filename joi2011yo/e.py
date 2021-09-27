from collections import deque
h,w,n = list(map(int,input().split()))

fig = []
fig.append("X"*(w+2))
for data in range(h):
  s = input()
  fig.append("X"+s+"X")
fig.append("X"*(w+2))

for i in range(len(fig)):
  for j in range(w+2):
    if fig[i][j] == "S":
      sy,sx = i,j

nQ = deque()
nQ.append([sy,sx])

for num in range(1,n+1):
  for gy in range(len(fig)):
    for gx in range(w+2):
      if fig[gy][gx] == str(num):
        nQ.append([gy,gx])

dist = []
time = 0

for N in range(1,n+1):
  
  dist = []
  for distance in range(w+2):
    dist.append([-1]*(w+2))
  
  SY,SX = nQ.popleft()
  GY,GX = nQ[0]
  
  dist[SY][SX] = time
  
  que = deque()
  que.append([SY,SX])
  
  while len(que) > 0:
    py,px = que.popleft()
  #上下左右の４方向を確認するテクニックで、４方向の(x,y)を取得
    for py2,px2 in [[py+1,px],[py-1,px],[py,px+1],[py,px-1]]:
  #行列の範囲内かを確認
      if not (0 <= py2 <= h+2) and (0 <= px2 <= w+2):
        continue
  #４方向の行き先が壁"#"でないかを確認
      if fig[py2][px2] == "X":
        continue
  #問題なければ、未訪問かを確認
      if dist[py2][px2] == -1:
    #未訪問の場合、隣接している頂点の距離＋１の値をインプット
        dist[py2][px2] = dist[py][px] + 1
      #キューに現在の頂点情報をappend
        que.append([py2,px2])
    time = dist[GY][GX]
print(dist[GY][GX])
