N = int(input())
NL = list(str(N))
n = [int(i) for i in NL]
print("Yes" if N%(sum(n))==0 else "No")
