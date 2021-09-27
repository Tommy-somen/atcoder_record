s = input()
s = s.replace("/","")
print("Heisei" if int(s) <= 20190430 else "TBD")
