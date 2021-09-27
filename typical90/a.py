n = int(input())

request = []
history = {}
order = []

for _ in range(n):
  req = input()
  request.append(req)
  
non_duplicate_request = list(set(request))

for register in non_duplicate_request:
  history[register] = False
  
for i in range(n):
  #print(history)
  if history[request[i]] == False:
    history[request[i]] = True
    order.append(i+1)

for number in order:
  print(number)
