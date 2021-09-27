N,M = map(int,input().split())
A = list(map(int,input().split()))
count = 0
A_sum =sum(A)
vote_min = A_sum/(4*M)
for i in range(len(A)):
  if A[i] >= vote_min:
    count += 1
print("Yes" if count >= M else "No")
