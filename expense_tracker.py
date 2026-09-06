Expense =[]

while True:
       
       category=input("Enter the category of the expense.\n")
       
       if category == "finish":
                     break
       price=float(input("Enter the price.\n"))
       expense={}
       expense["category"]= category
       expense["price"]=price
       
       Expense.append(expense)
       

       print(expense)
        
count=0
for i in range (len(Expense)):
 z=Expense[i].get("price")
 count+=z

print(f"The total amount spent is {count}")
       