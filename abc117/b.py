n = int(input())
L = list(map(int,input().split()))
L_max = max(L)
L_sum = sum(L)
print('Yes' if L_max < (L_sum-L_max) else 'No')