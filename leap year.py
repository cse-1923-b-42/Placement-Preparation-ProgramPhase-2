#Program to check leap year
"""
year = int(input("Enter a year"))
if (year % 400)==0:
    print("This is a leap year")
else:
    if ((year % 4)==0 and (year % 100)!=0):
        print("This is leap Year")
    else:
        print("This is not a leap Year")

input() """

x = int(input("Enter an Year"))
res = "Leap Year" if x%400==0 else "leap Year" if x%4==0 and x%100!=0 else "Non Leap Year"
print(res)
