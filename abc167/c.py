#入力部
n,m,x = map(int,input().split())
a = []
c = []
for s in range(n):
	c_tmp,*a_tmp = list(map(int,input().split()))
	c.append(c_tmp)
	a.append(a_tmp)
#ビット全探索処理
c_ans = []
for i in range(2**n):
	ans_box = [0]*m
	c_box = 0
	for j in range(n):
		if(i>>j)&1 == 1:
			for p in range(m):
				ans_box[p] += a[j][p]
			c_box += c[j]
	if min(ans_box) >= x:
		c_ans.append(c_box)
#出力部
print(min(c_ans) if len(c_ans)>0 else -1)
