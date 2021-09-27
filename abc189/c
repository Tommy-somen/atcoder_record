n = int(input())
a = list(map(int,input().split()))
 
ans_box = []

min_ver = 0
tmp_ans = 0

for i in range(n):

  len_cnt = 0
  min_val = a[i]

  for j in range(i,n):

    if min_val > a[j]:
      min_val = a[j]

    len_cnt += 1
    tmp_ans = max(min_val*len_cnt,tmp_ans)
      
print(tmp_ans)
