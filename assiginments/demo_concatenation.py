custName = "Manish "
itemDesc = "wants to purchase shirt"
tax = 3
price = 12
quantity = 2
print(type(itemDesc))
itemDesc = itemDesc[:18]+ str(quantity) + itemDesc[17:]
print(type(itemDesc))
message = custName +" "+ itemDesc
print(message)

total_cost = "Total cost with tax is:"+str(tax*price*quantity)
print(total_cost)
outofstock = False
if quantity >= 1:
    message = message +"s"
    print(message)
if outofstock:
    print("item is unavailable")
else:
    print("item is available")
shirt = ["Shirt","Tshirt","Denim","Sweat"]
print(len(shirt))
print(shirt[0])
print(shirt[4])
