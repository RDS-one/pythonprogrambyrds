#making a division calc
#number1=float(input("enter your divident:"))
#umber2=float(input("enter your divisor: "))
#print(f"when {number1} gets divided by {number2} is {number1/number2}")


#making a leap year calculator
#year=int(input("enter the year which you want to check: "))
#if year % 4 ==0:
#   if year/400:
 #       print(f"{year} was a leap year")
 #   else:
 #       print(f"{year} was not a leap year")    
#else:
   # print(f"{year} was not a leap year")

#making username and password username=Rugved password=RDS@1210\
username='itsme'
password='rugved'
username1=input("enter your username")
password1=input("enter your password")
if password == password1 and username == username1:
    print("your username and password were matched")
elif password != password1 and username == username1:
    print("your password was not matches but username was")
else:
    print("your nothing is matches")