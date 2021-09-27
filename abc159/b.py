S = input()
N = (len(S)-1)//2
M = (len(S)+3)//2
count = 0

if S[::-1] == S:
  if S[:N] == S[:N][::-1]:
    if S[(M-1):] == S[(M-1):][::-1]:
      count += 1
print("Yes" if count == 1 else "No")
