##愚直に組合せを計算すると、O(N^3）になるので、1番目の条件を満たして、
##2番目を満たないものを除算する方式をとる
n = int(input())
s = list(input())
##総数を計算
ans = s.count("R")*s.count("G")*s.count("B")
#(i,j)を固定してkを算出
for i in range(n):
    for j in range(i+1,n):
        k = 2*j - i
        ##indexはn-1までなのでkがn以上になるとbreak
        if k >= n:
           break
        ##kは2番目の条件を満たしていないものであるので、ここで条件1番が満たされているかをチェック
        if s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
          ans -= 1
       ##満たされていればこれは1番目を満たし、2番目を満たしていないものとなる　　　
print(ans)
