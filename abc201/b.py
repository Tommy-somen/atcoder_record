n = int(input())
st = [list(map(str,input().split())) for _ in range(n)]

name = []
mou = []

for N in st:
  N[1] = int(N[1])
  
st.sort(key=lambda x:x[1])

print(st[-2][0])
