print("Tip Calculator")
# totalBill=float(input("what was the total bill? $"))
# totalPeople=int(input("how many people to split the bill? "))
# totalWithOutTip=totalBill/totalPeople
# percentage=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# totalTip=totalWithOutTip+(totalWithOutTip*percentage/100)
# print("Each person should pay: $",round(totalTip,1))

#############
number = input("type a two digit number ")
print(int(number[0])+int(number[1]))
newInt = int(number)
print(round(newInt/10+newInt % 10))
