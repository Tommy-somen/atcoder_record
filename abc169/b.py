a=int(input())
b=input().split(" ")
sum1=1
 
if "0" in b:
    print("0")
else:
    for i in range(a):
        sum1=sum1*int(b[i])
        if sum1>10**18:
            sum1=-1
            break
    print(sum1)
