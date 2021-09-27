import sys
n,k = list(map(int,input().split()))
ab = [list(map(int,input().split())) for _ in range(n)]
ab.sort(key=lambda x:(x[0],x[1]))
#ab.sort(key=lambda x:x[1])
#print(ab)

cnt = 0
now_money = k

if now_money >= ab[0][0]:
  cnt += ab[0][0]
  now_money -= ab[0][0]
  now_money += ab[0][1]
#print(now_money)

for i in range(1,n):
  #print("##################")
  if (now_money+cnt) >= ab[i][0]:
    #print(now_money + cnt , ab[i][0])
    cnt = ab[i][0]
    #print("cnt:",cnt)
    #sub = now_money - (now_money-(ab[i][0]-cnt))
    #print("sub:",sub)
    now_money -= (cnt-ab[i-1][0])
    now_money += ab[i][1]
    #print("更新後",now_money)
  else:
    cnt += now_money
    print(cnt)
    sys.exit()

cnt += now_money
print(cnt)
