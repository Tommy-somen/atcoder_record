import math
n = int(input())

#約数列挙

div = []
num = 1

while(num <= int(math.sqrt(n))):
    if n%num == 0:
       div.append([str(num),str(n//num)])
    num += 1

#桁数の最小値を求める
ans = 10

for items in div:
    a_digit = len(items[0])
    b_digit = len(items[1])
    if ans > max(a_digit,b_digit):
        ans = max(a_digit,b_digit)

print(ans)
