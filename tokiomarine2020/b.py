A,V = map(int,input().split())
B,W = map(int,input().split())
T = int(input())
if W == V:
	print("NO")
else:	
	print("YES" if (T*(V-W)) >= abs(A-B) else "NO")
