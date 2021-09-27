import itertools
import math
import copy
n = int(input())
x_y= [list(map(int,input().split())) for X in range(n)]

#n!を作成
n_sum = math.factorial(n)
#n個の要素で順列を作成
n_list = list(itertools.permutations(x_y,n))
ans = 0
#順列を選択
for i in range(len(n_list)):
	#順列内の要素を順番通りに選択し、ansに加算する
	#繰り返し回数はlen(n_list)-1
	tmp = copy.copy(n_list[i])
	for j in range(n-1):
		ans += math.sqrt((tmp[j][0] - tmp[j+1][0])**2 + ((tmp)[j][1] - tmp[j+1][1])**2)
print('{:.10f}'.format((ans/n_sum)))
