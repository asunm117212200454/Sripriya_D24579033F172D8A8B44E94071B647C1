
def isLeapyear(year):
  if(year%400==0 or (year%4==0 and year%100!=0)):
    return True
  else:
    return False 
year=int(input("enter a year:"))
if isLeapyear(year):
  print("This is a leap year.", format(year))
else:
  print ("This is not a leap year.",format(year))