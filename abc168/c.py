import math
a,b,h,m = map(int,input().split())
angle = max((h*30+m*0.5),(m*6)) - min((h*30+m*0.5),(m*6))
angle = min(angle,(360-angle))
ans = (a**2) + (b**2) - (2*a*b*math.cos(math.radians(angle)))
print(math.sqrt(ans))
