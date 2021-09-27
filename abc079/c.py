import sys
num = list(input())
op1 = "+"
for x in range(2):
  op2 = "+"
  for y in range(2):
    op3 = "+"
    for z in range(2):
      fml = (num[0]+op1+num[1]+op2+num[2]+op3+num[3])
      if eval(fml) == 7:
        print(num[0]+op1+num[1]+op2+num[2]+op3+num[3]+"=7")
        sys.exit()
      op3 = "-"
    op2 = "-"
  op1 = "-"
