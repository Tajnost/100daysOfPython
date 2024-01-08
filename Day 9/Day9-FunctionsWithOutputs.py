

#########
#
#
# RETURN REPLACES THE FUNCTION IT CALLED !!!!

# Functions with Outputs

def format_name(firstName, lastName):
    if firstName == "" or lastName == "":
        return "You did't provide valid inputs"
    formatedfirstName = firstName.title()
    formatedlastName = lastName.title()  
    return f"{formatedfirstName} {formatedlastName}"

formated_string = format_name("Evelyn", "EVELYN")
print(formated_string)


################
# Days In Month 
################

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year,month):
  if is_leap(year) == False:
      month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  else:
      month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  return month_days[month-1]
  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)