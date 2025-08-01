units=int(input("Enter a number of units:"))
if units<=50:
    ammount=units*2.60
    tax=25.0
elif units<=100:
    ammount=130+(units-50)*3.25
    tax=35.0
elif units<=200:
    ammount=130+162.5+(units-100)*5.26
    tax=45
else: 
    ammount=130+162.5+526+(units-200)*8.45
    tax=75
total=ammount+tax
print("Your electricity is equal to",total)