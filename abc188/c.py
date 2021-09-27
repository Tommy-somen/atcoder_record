import copy

n = int(input())
get_players = list(map(int,input().split()))

players = copy.copy(get_players)

number = {}

for index in range(len(players)):
  number[players[index]] = True

while len(players) > 2:

  for i in range(0,len(players),2):
    if players[i] > players[i+1]:
      number[players[i+1]] = False
    else:
      number[players[i]] = False
  
  players = []

  for key,val in number.items():
    if val == True:
      players.append(key)

print(get_players.index(min(players))+1)
