#simple project for lists
shopping_list = ["dress","slippers","lipstick","bangle","food","dryfruits"]
while True:
  print("\n1.add item")
  print("\n2.remove item")
  print("\n3.display item")
  print("\n4. exit")
  choice = input("Enter your choice: ")
  if choice =="1":
    item = input("dress")
    shopping_list.append(item)
    print(item,"added!")
  elif choice == "2"
     item = input("food")
     if item in shopping_list:
       shopping_list.remove(item)
       print(item."remove")
    elif choice == "3":
        print("shoppping_list:",shopping_list)
    elif choice == "4":
        print("exit item")
    else:
       print("Inva;id choice: ")
       
       
