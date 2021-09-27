import copy
n,k = list(map(int,input().split()))
a = list(map(int,input().split()))

numbers = []
di_num = {}

sub = 0

if k >= n:
  sub = k//n
  k -= n*(k//n)

for _ in a:
  numbers.append(_)
  di_num[_] = sub
  
sort_numbers = copy.copy(numbers)
sort_numbers.sort()

if k > 0:
  for i in range(k):
    di_num[sort_numbers[i]] += 1
    
for j in range(n):
  print(di_num[numbers[j]])
