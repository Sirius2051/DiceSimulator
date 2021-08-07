import random

n_1 = " |     | \n  |  o  | \n  |     |"
n_2 = " | o   | \n  |     | \n  |   o |"
n_3 = " | o   | \n  |  o  | \n  |   o |"
n_4 = " |o   o| \n  |     | \n  |o   o|"
n_5 = " |o   o| \n  |  o  | \n  |o   o|"
n_6 = " |o   o| \n  |o   o| \n  |o   o|"

def main():
    dice_number = input("Please enter the number of dice you need, between one and seven: \n")

    try:
        n = int(dice_number)
    except:
        print("An error occurred, you did not enter a whole number")
        main()

    if n < 8:
        x = "y"
        faces = [n_1, n_2, n_3, n_4, n_5, n_6]
        dices_results = []
        while x == "y":
            for i in range(n):
                dices_results.append(random.randint(1, 6))

            for r in range(len(dices_results)):
#                 print(r)
                if dices_results[r] == 1:
                    print("The result is: 1 \n", n_1)
                elif dices_results[r] == 2:
                    print("The result is: 2 \n", n_2)
                elif dices_results[r] == 3:
                    print("The result is: 3 \n", n_3)
                elif dices_results[r] == 4:
                    print("The result is: 4 \n", n_4)
                elif dices_results[r] == 5:
                    print("The result is: 5 \n", n_5)
                elif dices_results[r] == 6:
                    print("The result is: 6 \n", n_6)
            print("The global result is: ", sum(dices_results))

            dices_results = []
            x = input("press 'y' to roll again or 'n' to exit\n")

    else:
        print("The number you entered is greater than expected")
        main()

main()
