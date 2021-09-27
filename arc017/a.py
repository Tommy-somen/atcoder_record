input_n = int(input())

n = 1000000

#2~nまでの数字列を作成
NumberList = [i for i in range(2,n+1)]
#素数列の入れ物を作成
PrimeList = []

#√n*√n=nの性質を利用すると、nまでの数列に√n以上の素数を利用した
#合成数がないため、2~√nまで探索して各探索数jの倍数をNumberListから排除する
while NumberList[0]**2 <= n:
#数字列の初項は合成数ではないため、素数列に追加する
  PrimeList.append(NumberList[0])
  #appendした素数を用いている合成数を排除したNumberListを作成する
  NumberList = [j for j in NumberList if j%NumberList[0] != 0]

#√nまでの素数列PrimeList + 合成数を排除した残りのNumberListを連結する
PrimeList.extend(NumberList)

if input_n in PrimeList:
  print("YES")
else:
  print("NO")
