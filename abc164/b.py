a,b,c,d = map(int,input().split())
#a = Takahashi's HP,b = T's ATK, c = Aoki's HP, d = A's ATK
#T -> A -> T -> A...
print("Yes" if -(-a//d) >= -(-c//b) else "No") 
