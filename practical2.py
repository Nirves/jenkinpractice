a=input("Enter Amout in Double")
money=float(a)
print("Your Amount",money,"Consist of")

dollars=money//1
money=money%1
money=round(money,2)

quarters=money//0.25
money=money%0.25
money=round(money,2)

dimes=money//0.1
money=money%0.1
money=round(money,2)

nickels=money//0.05
money=money%0.05
money=round(money,2)

print(money)
pennies=money//0.01

print(dollars,"DOLLOARS")
print(quarters,"QUARTERS")
print(dimes,"DIMES")
print(nickels,"NICKELS")
print(pennies,"PENNIES")

