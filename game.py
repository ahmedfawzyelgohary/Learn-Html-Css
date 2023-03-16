import random
 
range_top = input("please enter a number: ")
if range_top.isdigit():
    range_top=int(range_top)
    if range_top <= 0:
      print("please enter a number greater than 0")
      quit()
else:
    print("please enter a number!")
    quit()

random_number=random.randint(0,range_top)
guesses = 0

while True:
    guesses +=1
    user_guesses=input("Please Make A Guesses!")
    if user_guesses.isdigit():
        user_guesses=int(user_guesses)
    else:
        print("Please Eater A Number Next Time!")
        continue
    if user_guesses == random_number:
        print("Good Job")
        break
    elif user_guesses > random_number:
        print("Its Above !")
    else:
        print ("its below!")

print(f"your gusees is {guesses}")
            
     
