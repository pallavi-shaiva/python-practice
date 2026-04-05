balance = 1000
print("welcome to ATM")
print("1.check balance")
print("2.deposit money")
print("3.withdraw money")
choice = int(input("Enter your choice(1-3):"))
if choice == 1:
  print("your balance is:",balance)
elif choice == 2:
  deposit = int(input("Enter ampunt to deposit: "))
  balance = balance + deposit
  print("updating balance:",balance)
elif chice == 3:
  withdraw = int(input("Enter amount to withdraw: "))
  if withdraw <= balance:
    balance = balance - withdraw
    print("please collect your cash")
    print("remaining balance:",balance)
  else:
    print("Insufficient balance")
else:
  print("Invalid choice")
