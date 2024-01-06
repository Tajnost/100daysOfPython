n = int(input()) # Check this number

def prime_checker(number):
  checker = 0

  if number == 1 or number == 2 or number == 3 or number == 5:
    number2 = [1,2,3,5] 
  else:
    number2 = [1,2,3,5,number] 
    
  if number == 0 or number == 1:
    print("It's not a prime number.")
  else:
    for i in range(len(number2)):
      divisibility = number % number2[i]
      print(divisibility)
      if divisibility == 0:
        checker += 1
    if checker == 2:
      print("It's a prime number.")
    else:
      print("It's not a prime number.")
    

prime_checker(number=n)