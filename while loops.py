# while loop:
i = 1
while i <= 5:
  print(i)
  i += 1
#common example:counting sheep:
sheep_count = 1
while sheep_count <= 10:
  print(f"sheep {sheep_count}")
  sheep_count +=1
#avoinding infinite loops:
i = 1
while i <= 5:
  print(i)
#using break :
sheep_count = 
while sheep_count <= 10:
  print(f"sheep {sheep_count}")
  if sheep_count == 5:
    print("thats enough counting!")
    break
  sheep_count += 1
  #using continue:
  sheep_count = 1
  while sheep_count <= 5:
    if sheep_count == 4:
      sheep_count += 1
      continue
    print(f"sheep {sheep_count}")
    sheep_count += 1
    #using while lopps for user input:
    pin = ""
    correct_pin = "123456"
    while pin != correct_pin:
      pin = input("Enter your pin:")
      if pin != correct_pin:
          print("incorrect pin.try again.")
      print("pin accepted.you can proceed.")
    #KSRTC example:
    available_seats = 5
    while available_seats > 0:
      print(f"{available_seats} seats available.")
      booking = input("do you want to book a seat? (yes/no): ").lower()
      if booking == "yes":
          available_seats -=1
          print("seat booked!")
      else:
          print("no booking made.")
    print("all seats are booked!")
  #nested while loops:
  while snacks_available > 0 and money > 0:
    print(f"snacks available: {snacks_available}. money: {money}")
    buy = input("do you want to buy a snack for rupes 5? (yes/no: ").lower()
    if buy == "yes" and money >= 5:
      snacks_available -=1
      money -=5
      print("snack purchase  made.")
  print("Either snacks are sold out or you are out of money.")
