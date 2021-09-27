from collections import deque
import math
n = int(input())

#10^10は10^5^2までなので、繰り返しは10^5まで
#乗数は2^34で、10^10を越すので、34
#よって、二重ループした際の計算量はO(10^5＊34)=O(10^6)

cnt = deque()

N = int(math.sqrt(n))


for i in range(2,N+1):
	for j in range(2,34):
		if i**j <= n:
			cnt.append(i**j)
			
ans = len(list(set(cnt)))
print(n - ans)
