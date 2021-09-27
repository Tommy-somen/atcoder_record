from collections import deque

h,w = list(map(int,input().split()))

#図情報の取得
fig = []
fig.append("#"*(h+2))
for _ in range(h):
  s = input()
  s = "#"+s+"#"
  fig.append(s)
fig.append("#"*(h+2))

#状態情報の作成　→　全てー１とする
dist = []
dist.append([0]*(w+2))
for D in range(h):
  dist.append([-1]*(w+2))
dist.append([0]*(w+2))


#黒色情報の取得
black = []
for B in range(1,h+1):
  for W in range(1,w+1):
    if fig[B][W] == "#":
      black.append([B,W])

#黒色情報箇所の状態更新　→黒色になった時に１と更新する
for i,j in black:
  dist[i][j] = 0

#キューの作成
Q = deque(black)

#幅優先探索法
#キューに頂点情報がある限りループ
while len(Q) > 0:
#キューの左側を頂点情報として取得
  py,px = Q.popleft()
  #上下左右の４方向を確認するテクニックで、４方向の(x,y)を取得
  for py2,px2 in [[py+1,px],[py-1,px],[py,px+1],[py,px-1]]:
  #行列の範囲内かを確認
    if not (1 <= py2 <= h) and (1 <= px2 <= w):
      continue
  #４方向の行き先が壁"#"でないかを確認
    if fig[py2][px2] == "#":
      continue
  #問題なければ、未訪問かを確認
    if dist[py2][px2] == -1:
    #未訪問の場合、隣接している頂点の距離＋１の値をインプット
      dist[py2][px2] = dist[py][px]+1
      #キューに現在の頂点情報をappend
      Q.append([py2,px2])
      
ans = 0
for distance in dist:
  mx = max(distance)
  ans = max(ans,mx)
print(ans)
