Alp =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]*2
N = int(input())
S = list(input())
for i in range(len(S)):
	Anum = Alp.index(S[i])
	S[i] = Alp[Anum+N]
print("".join(S))
