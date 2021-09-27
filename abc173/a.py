import sys
n = int(input())
for i in range(100):
  if 1000*i >= n:
    print(1000*i - n)
    sys.exit()
