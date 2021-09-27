x = int(input())
#ゴリ押し解法
mny = 100
count = 0
while(x > mny):
	mny += int(mny*0.01)
	count += 1
print(count)
