Expense =[]

while True:
       print("1. Add expense")
       print("2. View expense")
       print("3. View total")
       print("4. Delete")
       print("5. Exit")
      
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
       elif option =="4":
           
            for number,detail in enumerate(Expense,start=1):
               print(number,detail)
            try:
                
                     
                  index=int(input("Enter the index.\n"))
                  Expense.pop(index-1)
                  print("Expense deleted")
                  print(Expense)
            except IndexError:

                print("Invalid input")
            
            
             
       if option =="5" :
                     break
       

