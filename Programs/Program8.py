#  Leap year  == 366


year = int(input("Enter  year"))
if (year % 400 == 0) and (year% 100 == 0):
    print(year,"It's A Leap Year")
elif (year %4 == 0) and (year %100 != 0):
    print(year,"It's A leap Year")
else:
    print("It's Not A Leap Year")

    