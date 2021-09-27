sx,sy,gx,gy = list(map(int,input().split()))

ans = -sy*((sx-gx)/(sy+gy))+sx

print(ans)
