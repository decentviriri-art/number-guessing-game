import random

choice_comp = random.randint(1,20)
count=0
while True:
  user = int(input("Enter number:"))
  count +=1

  if choice_comp== user:
      print("Congrats good guess")
      print(f"Number of guesses: {count}")
      print(f"Computer guess :{choice_comp}")
      break
  elif choice_comp < user:
      print("guess is too high")
     
  else:
    print("Guess is too low")
  

