def isLeapYear (year):
 if (year%4==0 and year%100!=0)or year%400==0:
     return
 else:
  return False 
year=int(input("Enter a year:"))
if isLeapYear(year):
  print('{}is a LeapYear.'.format(year))
else:
  print('{}is a LeapYear.'.format(year))


  


