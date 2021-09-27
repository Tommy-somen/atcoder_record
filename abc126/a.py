n,k = map(int,input().split())
s = list(input())
s[k-1] = s[k-1].lower()
print("".join(s)) #"".join()にてリストを文字列に変換できる
