from collections import Counter
 
N = int(input())
A = list(map(int,input().split()))

#各数字が何個ずつ出現しているかを確認する　→ {1:x, 2:y, 3:z...}
A_cnt = Counter(A)
ans = 0

#Aは,|A|<=200の制約上、-200 <= Ai <= 200となるため、この範囲の組合せの(Ai-Aj)**2しか出現しない。
for x in range(-200, 201):
  for y in range(x+1, 201):
    #Counterは辞書型のため、dict[x]により、キーxでの個数を検索できる。
    #つまり、順にxが進み、Aに存在するxになったとき、その個数をcxとして取得する
    cx = A_cnt[x]
    #yも同様
    cy = A_cnt[y]
    
    #cx,cy > 0の時、組合せが1つ以上存在するため、これに、(x-y)**2をかける
    #もしも cx,cy < 1の時、積は0となるため、加算されても問題なし。
    ans += cx*cy*(x-y)**2
    
print(ans)
