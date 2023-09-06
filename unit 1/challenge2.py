def isLeapYear (year):
 return year % 4 == 0
year= int(input("Enter a year: "))  
if isLeapYear (year):
   print( year, "is a leap year")
else:
   print(year," is not a leap year")