n,k = list(map(int,input().split()))

head = k

ans = head * ((head-1)**(n-1))

print(ans)
