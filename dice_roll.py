import random

min_val = 1
max_val = 6

roll_again = input()

while roll_again == "yes" or roll_again == "y":
    print("Dices rolling...")
    print("The values are :")

    # print randomly generated number
    print(random.randint(min_val, max_val))
    # print randomly generated number 2nd die
    print(random.randint(min_val, max_val))
    break

#roll_again = input("Roll the dice again? ")





