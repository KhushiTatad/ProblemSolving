#  Largest Number 


num1 = float(input("Enter First Number "))
num2 = float(input("Enter Second Number "))
num3 = float(input("Enter Third Number "))

if (num1 > num2) and (num1 > num3):
    print(num1, "Is The Largest Number ")
    
elif (num2 > num1) and (num2 > num3):
    print(num2, "Is The Largest Number ")

else : 
    print(num3, "Is The Largest Number")