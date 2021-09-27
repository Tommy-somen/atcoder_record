O = list(input())
E = list(input())

PASSWORD = []

O_len = len(O)
E_len = len(E)

len_max = max(O_len,E_len)

for i in range(len_max):
  if i+1 <= O_len:
    PASSWORD.append(O[i])
  
  if i+1 <= E_len:
    PASSWORD.append(E[i])

print("".join(PASSWORD))
