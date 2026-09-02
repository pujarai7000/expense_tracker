Expense=[]
prices=[]

while True:
       
       category=input("Enter the category of the expense.\n")
       
       if category == "finish":
                     break
       price=float(input("Enter the price.\n"))
       Expense.append(category)
       prices.append(price)
       print(Expense)
       print(prices)


amount= float(sum(prices))
print(f"The total amount spent is {amount}")
       