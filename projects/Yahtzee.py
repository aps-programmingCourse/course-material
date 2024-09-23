#!/usr/bin/python3
import random, os 

blue = "\033[1;34m"
red = "\033[1;31m"  
green = "\033[0;32m"
reset = "\033[0;0m"

print(blue)
print("Welcome to Yahtzee! \nYou'll need either 5 digital or real dice to play.")
print("")
print("You can roll up to 3 times for every turn.\nThe objective is to get as many points in each category as possible")
print("For example, you will try to get 5 ones in the ones category. \n")
print(reset)

def playYahtzee():
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0

    threeOfKind = 0
    fourOfKind = 0
    smallStraight = 0
    largeStraight = 0
    fullHouse = 0
    yahtzee = 0
    chance = 0

    bonus = 0

    categoryList = [ones, twos, threes, fours, fives, sixes, threeOfKind, fourOfKind, smallStraight, largeStraight, fullHouse, yahtzee, chance]

    while True:

        print("These are the categories that you can roll for:\n")

        print(green, "1. Ones: ", red + str(ones), reset)
        print(green, "2. Twos: ", red + str(twos), reset)
        print(green, "3. Threes: ", red + str(threes), reset)
        print(green, "4. Fours: ", red + str(fours), reset)
        print(green, "5. Fives: ", red + str(fives), reset)
        print(green, "6. Sixes: ", red + str(sixes), reset)

        print("")

        if ones > 0 and twos > 0 and threes > 0 and fours > 0 and fives > 0 and sixes > 0:
            print(blue, "Sum of top section: ", ones+twos+threes+fours+fives+sixes, reset)
            if ones+twos+threes+fours+fives+sixes >= 63:
                bonus += 35
                print(red, "BONUS: 35", reset)

        print("")

        print(green, "7. Three of a kind (Total of all dice): ", red + str(threeOfKind), reset)
        print(green, "8. Four of a kind (Total of all dice): ", red + str(fourOfKind), reset)
        print(green, "9. Small Straight (30 points): ", red + str(smallStraight), reset)
        print(green, "10. Large Straight (40 points): ", red + str(largeStraight), reset)
        print(green, "11. Full House (25 points here if you get 3 of one number and 2 of another): ", red + str(fullHouse), reset)
        print(green, "12. Yahtzee (100 if you get all the same number): ", red + str(yahtzee), reset)
        print(green, "13. Chance (face value of all your dice): ", red + str(chance), reset)

        print("")

        if threeOfKind > 0 and fourOfKind > 0 and smallStraight > 0 and largeStraight > 0 and fullHouse > 0 and yahtzee > 0 and chance > 0: 
            print(blue, "Sum of bottom section: ", threeOfKind+fourOfKind+smallStraight+largeStraight+fullHouse+yahtzee+chance, reset)

        if ones > 0 and twos > 0 and threes > 0 and fours > 0 and fives > 0 and sixes > 0 and threeOfKind > 0 and fourOfKind > 0 and smallStraight > 0 and largeStraight > 0 and fullHouse > 0 and yahtzee > 0 and chance > 0:
            print(blue, "Your final score is: ", ones+twos+threes+fours+fives+sixes+threeOfKind+fourOfKind+smallStraight+largeStraight+fullHouse+yahtzee+chance+bonus, reset)
            print("Thanks for playing!")
            break


        category = input("Pick a category: ")
        diceRoll = input("Score: ")

        print("")

        if category == "1":
            if ones == 0:
                ones += int(diceRoll)
            else:
                print(red)
                print("The ones category has already been used")
                print(reset)

        if category == "2":
            if twos == 0:
                twos += int(diceRoll)
            else:
                print(red)
                print("The twos category has already been used")
                print(reset)

        if category == "3":
            if threes == 0:
                threes += int(diceRoll)
            else:
                print(red)
                print("The threes category has already been used")
                print(reset)

        if category == "4":
            if fours == 0:
                fours += int(diceRoll)
            else:
                print(red)
                print("The fours category has already been used")
                print(reset)

        if category == "5":
            if fives == 0:
                fives += int(diceRoll)
            else:
                print(red)
                print("The fives category has already been used")
                print(reset)

        if category == "6":
            if sixes == 0:
                sixes += int(diceRoll)
            else:
                print(red)
                print("The sixes category has already been used")
                print(reset)


        if category == "7":
            if threeOfKind == 0:
                threeOfKind += int(diceRoll)
            else:
                print(red)
                print("The three of a kind category has already been used")
                print(reset)

        if category == "8":
            if fourOfKind == 0:
                fourOfKind += int(diceRoll)
            else:
                print(red)
                print("The four of a kind category has already been used")
                print(reset)

        if category == "9":
            if smallStraight == 0:
                smallStraight += int(diceRoll)
            else:
                print(red)
                print("The small straight category has already been used")
                print(reset)

        if category == "10":
            if largeStraight == 0:
                largeStraight += int(diceRoll)
            else:
                print(red)
                print("The large straight category has already been used")
                print(reset)

        if category == "11":
            if fullHouse == 0:
                fullHouse += int(diceRoll)
            else:
                print(red)
                print("The full house category has already been used")
                print(reset)

        if category == "12":
            if yahtzee >= 100:
                yahtzee += 100
            elif yahtzee == 0:
                yahtzee += int(diceRoll)
            else:
                print(red)
                print("The yahtzee category has already been used")
                print(reset)

        if category == "13":
            if chance == 0:
                chance += int(diceRoll)
            else:
                print(red)
                print("The chance category has already been used")
                print(reset)

        
        os.system('clear')

playYahtzee()
