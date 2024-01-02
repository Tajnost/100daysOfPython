print("Welcome to the tip calulator \n\n")

totalBill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
split = input("How many people to split the bill? ")

tipCalculated = int(tip) / 100 * int(totalBill)
splitBill = (float(totalBill) + float(tipCalculated)) / int(split)
splitBillRound = round(splitBill,2)
splitBillRound = "{:.2f}".format(splitBill)

print(f"Each person should pay: ${splitBillRound}")