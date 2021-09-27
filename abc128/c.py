n,m = map(int,input().split())
klist = []
swlist = []
ans = 0
for s in range(m):
	k,*sw = list(map(int,input().split()))#kとswを別々に入力
	klist.append(k) #<- kのリスト
	swlist.append(sw) #<- swのリスト
pwlist = list(map(int,input().split())) #pwのリスト

for i in range(2**n):#0~2**nまでの整数をカウントする(整数→ビットでの全探索)
	check = True
	for lump in range(m):#m個の電球についてカウントする
		cnt = 0
		for j in range(klist[lump]):#各スイッチ内の右シフト数をカウント	
			if (i>>swlist[lump][j]-1)&1==1:#右にjシフトする
				cnt += 1#整数iのビットに対し、klistのスイッチがいくつonかをカウントする
		if cnt%2 != pwlist[lump]:#一つのスイッチ列でのカウント終了につき、判定する
			check = False#pwと互換性が1つでもなければFalseとする
	if check == True:#最後までFalseにならなければ組み合わせがあるということになる
		ans += 1
print(ans)
