k = int(input())
a,b = list(map(str,input().split()))

def Base_n_to_10(X,n):
  out = 0
  for i in range(1,len(str(X))+1):
    out += int(X[-i])*(n**(i-1))
  return out

A = Base_n_to_10(a,k)
B = Base_n_to_10(b,k)

print(A*B)
