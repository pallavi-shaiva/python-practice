#number_toolkit.py
# A simple loo-based python project
def multiplication_table():
  num= int(input("ENter a number: "))
  print(f"\n multiplication table of {num}:")
  for i in range (1,11):
    print(f"{num} x {i} = {num * i}")
def factorial():
  num=int(input("Enter a number: "))
  fact = 1
  for i in range(1,num +1):
      fact *= i
  print(f"factorial of{num} is{fact}")
def check_prime():
  num=int(input("Enter a number: "))
  if num <= 1:
    print("it is not a prime number")
    return
  for i in range(2,int(num ** 0.5)+1):
    if num & i ==0:
      print("it is not a prime number.")
      return
  print("it is a prime number.")
  def sum_natural_numbers():
    num=int(input("Enter a number:"))
    total= 0
    for i in range(1,num +1):
      total+=1
    print(f"sum of firts {num} natural number is{total}")
  #main progarm using while loops:
  while True:
    print("\n=====number toolkit menu =====")
    print("1.multiplication table")
    print("2.factorial of a number")
    print("3.check prime number")
    print("4.sum of natural numbers")
    print("5.exit")
    choice = input("Enter your choice(1-5):")
    if choice == "1":
      multiplication_table()
    elif choice == "2":
      factorial()
    elif choice == "3":
      check_prime()
    elif choice == "4":
      sum_natural_numbers()
    elif choice == "5":
      print("thank you for using number toolkit!")
      break
    else:
      print("invlid choice!please try again.")
