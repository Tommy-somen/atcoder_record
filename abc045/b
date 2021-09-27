sa = list(input())
sb = list(input())
sc = list(input())

move = sa.pop(0)

def check(lis):
  
  global move
  global flg

  if len(lis) != 0:
    move = lis.pop(0)
  else:
    flg = False

flg = True

while(flg):
  if move == "a":
    check(sa)
  elif move == "b":
    check(sb)
  else:
    check(sc)
    
print(move.upper())
