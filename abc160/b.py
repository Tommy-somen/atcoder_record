X = int(input())
happy = 0

if X//500 >= 1:
	happy += 1000*(X//500)
	X -= 500*(X//500)
if X//5 >= 1:
	happy += 5*(X//5)
	X -= 5*(X//5)
print(happy)
