from dice import Die, Dice

print("DICE ROLLER PROGRAM")
print("~"*20)
print()

count = int(input("How many dice do you want to roll? "))   # 5

dice = Dice()               # Dice object is dice
for i in range(count):      # 5 times
    die = Die()             # Die object is die 
    dice.addDie(die)        # add the Die object to the Dice.list using addDice() method

dice.rollAll()              # Roll All the die object
for die in dice.list:       # [4, 3, 1, 4, 5]
    print(die.value, end=" ")

