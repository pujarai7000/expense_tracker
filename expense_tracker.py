Expense =[]

while True:
       print("1. Add expense")
       print("2. View expense")
       print("3. View total")
       print("4. Exit")
       option=input("Choose option\n")
       
       
       if option=="1" :
          category=input("Enter the category.\n")
          price=float(input("Enter the price.\n"))
          expense={}
          expense["category"]= category
          expense["price"]=price
      
          Expense.append(expense)
          print(expense)
       elif option =="2":
             for detail in Expense:
              print(detail)
       elif option =="3":
           count=0
           for i in range (len(Expense)):
            z=Expense[i].get("price")
            count+=z

           print(f"The total amount spent is {count}")
             
       if option =="4" :
                     break
       

