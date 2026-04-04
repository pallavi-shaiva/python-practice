#simple project in use dictionaries:
contacts = {}
while True:
  print("\n1.add contact"
  print("2. search contact")
  print("3.update contact")
  print("4.delete contact")
  print("5.show all contact")
  print("6.exit")
  choice = input("Enter choice: ")
  if choice == "1":
    name = input("Enter name:")
    phone = input("Enter phone number: ")
    contacts[name] = phone
  elif choice == "2":
     name = input("Enter namae to search: ")
     if name in contacts:
       print(phone number:",contacts[name])
     else:
       print("contact not found")
   elif choice == "3":
     name = input("Enter name: ")
     if name in contacts:
         contacts[name]=input("Enter new number: ")
     else:
       print("contact not found")
   elif choice == "4":
     name = input("Enter name:")
     if name in contacts:
       del contacts[name]
       print("deleted successfully")
     else:
       print("contact not found")
   elif choice == "5":
     print("\ncontacts list:")
     for name,phone in contacts.items():
       print(name,":",phone)
   elif choice == "6"
       print("Invalid choice") 

     
    
