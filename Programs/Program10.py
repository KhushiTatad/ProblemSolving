#  Prime Number 

num = int(input("Enter Number "))

if num == 1 :
    print("Prime Number ")

elif num == 2 :
    print("Not A Prime")


if num > 1:
    for i in range (2,num):
        if num % i == 0 :
            print("Not A Prime")
            break
    else :
         print("Prime Number ")