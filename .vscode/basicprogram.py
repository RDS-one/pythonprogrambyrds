#i went to mall i bought 4 product so this is a addition question 
#laptop=input("enter the price of laptop :")
#computer=input("enter the price of computer :")
#phone=input("enter the price of phone :")
#keyboard=input("enter the price of keyboard :")
#print(f"madam your total bill of laptop,computer,phone,keyboard would be {int(laptop)+int(computer)+int(phone)+int(keyboard)}")

#user_name='rugved'
#pass_word ='itsme'
#username=input("enter your username")
#password=input("enter your password")
#if password==pass_word:
#    if username != user_name:
#        print("your username was not correct")
#    else:
#        print("your username and password were matched")
#lse:
 #   print("your password was not matched ")

# admission criteria 
mathematics=int(input("enter your marks in mathematics :"))
physics=int(input("enter your marks in physics :"))
chemistry=int(input("enter your marks in chemistry :"))
addition=int(mathematics)+int(physics)
if mathematics >= 65 and physics >=55 and chemistry >=50:
    print("you were eligible ")
elif addition >= 140:
    print("you are still eligible")
else:
    print("sry you are not eligible")
