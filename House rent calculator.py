rent=int(input("Enter your flat rent:"))
food=int(input("Enter food charge:"))
electricity=int(input("Enter total electricity spend:"))
charge_per_unit=int(input("Enter chrge per unit:"))
persons=int(input("Enter total number of people living in flat:"))
total_bill=electricity*charge_per_unit
output=(food+rent+total_bill)// persons

print("Each person will pay:",output)
         