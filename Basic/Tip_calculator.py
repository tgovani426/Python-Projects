# tip calculator
print("Welcome to the tip calculator.")
amt=input("What was the amount of the bill? $")
tip = input("What percentage of tip would you like to give? 10, 12, or 15?")
no_people = input("how many people to split he bill?")

total_amt = float(amt)*(float(tip)/100) + float(amt)
total_bill=total_amt
final=round(total_bill,2)
print(f"Each person should pay: ${final}")
