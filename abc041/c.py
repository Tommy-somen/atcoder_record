n = int(input())
a = list(map(int,input().split()))
box = []
for i in range(0,n):
  box.append([i+1,a[i]])
box.sort(key=lambda x:x[1],reverse=True)
for j in range(n):
  print(box[j][0])
