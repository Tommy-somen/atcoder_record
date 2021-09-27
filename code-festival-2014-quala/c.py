a,b = list(map(int,input().split()))

a_years = 0
a_years += ((a-1)//4)
a_years -= ((a-1)//100)
a_years += ((a-1)//400)
"""
if (a%4 == 0) and (a%100 != 0) or ((a%4 == 0) and (a%100 != 0) and (a%400 == 0)):
  a_years -= 1
"""


b_years = 0
b_years += ((b)//4)
b_years -= ((b)//100)
b_years += ((b)//400)


rslt = b_years - a_years

if rslt > 0:
    print(rslt)
else:
    print(0)
