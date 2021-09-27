import math
from decimal import *
a,b = map(float,input().split())
ans = Decimal(str(b))*int(a)
print(math.floor(ans))
