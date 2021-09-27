X = int(input())

n = X+1000

NumList = [i for i in range(2,n)]
Prime = []

j = 2

while (j*j <= n):
  Prime.append(NumList[0])
  NumList = [k for k in NumList if k%j != 0]
  j += 1

Prime.extend(NumList)

ANS = [p for p in Prime if p >= X]
print(ANS[0])  
