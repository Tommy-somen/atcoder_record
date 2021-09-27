import sys

s = list(input())

piano = ["Do","Re","Mi","Fa","So","La","Si"]
flg = False
cnt = -1

for i in range(len(s)-1):
  if s[i] == "W":
    cnt += 1
  if s[i] == s[i+1]:
    index = i+1
    if s[index+4] == s[index+5]: #SiDo MiFa
      print(piano[6-cnt])
      sys.exit()
    else:#MiFa SiDo
      if cnt > 2:
        tmp = cnt -2
        print(piano[-tmp])
        sys.exit()
      else:
        print(piano[2-cnt])
        sys.exit()
