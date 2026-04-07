#simple project for use while loops:
score = 0
i = 1
while i<= 3:
  if i == 1:
    answer = input("q1:what is 2 + 2?")
    if answer == "4":
      print("correct!")
      score += 1
    else:
  elif i == 2:
      answer = input("q2: capital of india? ")
      if amswer.lower() == "delhi":
        print("correct!")
        score += 1
      else:
         print("incorrect!")
   elif i == 3:
     answer = input("q3:python is a language? (yes/no)")
     if answer.lower() == "yes":
       print("correct!")
       score += 1
     else:
       print("incorrect!")
    i += 1
print("\n your final score is:",score)
             
    
