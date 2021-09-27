import sys
h,w = list(map(int,input().split()))
sys.setrecursionlimit(10**9)


#番兵付き平面情報の作成
fig = []
fig.append("#"*(w+2))
for _ in range(h):
  s = input()
  fig.append("#"+s+"#")
fig.append("#"*(w+2))

#スタート地点の取得
for i in range(len(fig)):
  for j in range(len(fig[i])):
    if fig[i][j] == "s":
      SY,SX = i,j

#訪問情報の作成
visited = []
for F in range(len(fig)):
  visited.append([False]*len(fig[F]))


#フラグの作成
flg = False

#DFSの作成
def dfs(ky,kx):
  global flg
  sy,sx = ky,kx
  visited[ky][kx] = True
  #print(visited)
  for py,px in [[sy+1,sx],[sy-1,sx],[sy,sx+1],[sy,sx-1]]:
    if fig[py][px] == "#":
      continue
    if visited[py][px] == True:
      continue
    if fig[py][px] == "g":
      flg = True
    dfs(py,px)

dfs(SY,SX)

#出力
if flg:
  print("Yes")
else:
  print("No")
