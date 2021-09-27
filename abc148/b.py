N = int(input())
S,T = map(str,input().split())
S = list(S)
T = list(T)
ST = []
for i in range(N):
  ST.append(S[i]+T[i])
print("".join(ST))
  
