n,Weight = list(map(int,input().split()))

weight_list = [0]
value_list = [0]

for wv in range(n):
  w,v = list(map(int,input().split()))
  weight_list.append(w)
  value_list.append(v)

value = [[-float("inf")]*(Weight+1) for _ in range(n+1)]
value[0][0] = 0

for i in range(1,n+1):
  for w in range(Weight+1):
   
    value[i][w] = max(value[i][w],value[i-1][w])
    
    if w - weight_list[i] >= 0:
      value[i][w] = max(value[i][w],value[i-1][w-weight_list[i]]+value_list[i])

print(max(value[n]))
