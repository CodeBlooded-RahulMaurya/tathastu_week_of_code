costPrice = float(input("Enter Cost Price of an item : "))
sellingPrice = float(input("Enter its Selling Price : "))
profitP = (sellingPrice-costPrice)*100/costPrice
print("Profit at ",sellingPrice,"Rs. is ",sellingPrice-costPrice,"Rs. and with ",profitP,"% profit.")
newSprice = 1.05*(sellingPrice-costPrice)+costPrice
print("To increase the profit by 5% the selling price should be ",newSprice," Rs. with ",profitP+5,"% profit.")
