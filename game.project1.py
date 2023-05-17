import random

list = ['s','w','g']

chance = 10
no_ofchance = 0
computer_point = 0
human_point = 0

print("***** WELCOME IN GAME ***** \n","    [Snake,Water,Gun,game] \n\n\n")
print("s : for snake\nw : for water\ng : for gun\n")

# inp = str(input("snake : water : gun :")())
while no_ofchance < chance:
     _input = input('snake, water, gun :')
     _random = random.choice(list)

     if _input == _random:
        print("Both 0 point to same \n ")

    # if user Enter s ....!
     elif _input == 's' and _random =='g':
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random}\n")
        print("computer wins 1 point \n ")
        print(f"computer points is {computer_point} and your point is {human_point}\n")

     elif _input == 's' and _random == 'w':
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random}\n")
        print("human wins 1 point \n ")
        print(f"computer points is {computer_point} and your points is {_input}\n")

     # if user enter w ...!
     elif _input == 'w' and _random == 's':
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random}\n")
        print("computer wins 1 point \n ")
        print(f"computer points is {computer_point} and your points is {_input}\n")

     elif _input == 'w' and _random == 'g':
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random}\n")
        print("you wins 1 point \n ")
        print(f"computer points is {computer_point} and your points is {_input}\n")

     elif _input == 'g' and _random == 's':
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random}\n")
        print("you wins 1 point \n ")
        print(f"computer points is {computer_point} and your points is {_input}\n")

     elif _input == 'g' and _random == 'w':
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random}\n")
        print("computer wins 1 point \n ")
        print(f"computer points is {computer_point} and your points is {_input}\n")

     else:
        print("you have input wrong \n")

     no_ofchance = no_ofchance + 1
     print(f"{chance - no_ofchance} is left out of {chance} \n")

     print("Game over")

if computer_point == human_point:
       print("both are winners")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")