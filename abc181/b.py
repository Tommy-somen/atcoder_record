n = int(input())

A = []
B = []

#a,bをそれぞれA,Bに格納
for _ in range(n):
  a,b = list(map(int,input().split()))
  A.append(a)
  B.append(b)
  
ans = 0

#左端と右端の数字から区間の総和を計算する。→Biまでの総和-Aiまでの総和
for i in range(n):
  #nまでの総和は、n*(n+1)//2である。またAiの総和は、Aiを含めないため、Ai-1までの総和とする
  B_sum = (B[i]*(B[i]+1))//2
  A_sum = (A[i]-1)*(A[i])//2
  ans += (B_sum - A_sum) 

print(ans)
