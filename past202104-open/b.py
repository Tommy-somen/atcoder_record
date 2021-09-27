import sys
s = list(input())
#リストの文字列を４文字ごとに区切り、joinで結合している
s_s = ["".join(s[i: i+4]) for i in range(0, len(s), 4)]

cnt = 0

for j in s_s:
  cnt += 1 
  if j == "post":
    print(cnt)
    sys.exit()

print("none")
