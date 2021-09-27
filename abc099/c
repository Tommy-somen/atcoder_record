import math

n = int(input())

dist = [float("inf") for distance in range(n+1)]
dist[0] = 0

for i in range(1,n+1):

  one = dist[i-1]+1
  
  if i >= 6:
    six = 6
    six_mul = float("inf")
    while(six <= i):
      six_mul = min(six_mul,dist[i-six]+1)
      six *= 6
    
    if i >= 9:
      nine = 9
      nine_mul = float("inf")
      while(nine <= i):
        nine_mul = min(nine_mul,dist[i-nine]+1)
        nine *= 9
      dist[i] = min(dist[i],one,six_mul,nine_mul)
    else:
      dist[i] = min(dist[i],one,six_mul)
  else:
    dist[i] = min(dist[i],one)

print(dist[n])
