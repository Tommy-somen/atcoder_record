n = int(input())

front,back = [],[]
i = 1

while i*i <= n:
	if n%i == 0:
		front.append(i)
		if i != n//i:
			back.append(n//i)
	i += 1
	
front.extend(back[::-1])

for k in front:
	print(k)
