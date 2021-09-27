S,T = map(str,input().split())
A,B = map(int,input().split())
U = input()

if T == U :
	print(A, B-1)

else :
	print(A-1,B)
