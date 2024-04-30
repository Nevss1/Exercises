import random
from time import sleep


def showresult(result, pchoice):
    if result is True:
        print(f"user \033[0:32mwin!\033[m Bot chose {choices[pchoice-1]}")
    else:
        print(f"user \033[0:31mlost!\033[m Bot chose {choices[pchoice-1]}")


def waitingtime(sec=0):
    for i in range(0, sec-1):
        sleep(0.5)
        print(".", end="")
    sleep(0.5)
    print(".")
    sleep(0.5)


def usrautentication():
    while True:
        user = input()
        if len(user) == 1 and user in "012":
            user = int(user)
            return user
        else:
            print("\033[0:31mError\033[m enter a valid value!")


wins = 0
matches = 0
while True:
    choices = ("Rock", "Paper", "Scissors")
    print("Your turn!")
    print("[1] Rock")
    print("[2] Paper")
    print("[3] Scissors")
    usr = usrautentication()  # verify if user puts a int value for choices
    sleep(0.5)
    print("bot is choosing", end="")
    waitingtime(3) # puts three dots after choosing
    pc = random.randint(1, 3)
    matches += 1
    if usr == pc:  # TIE
        print(f"\033[0:30:44mTIE!\033[m both players chose {choices[pc-1]}")
    elif usr == 1:  # USR PUTS ROCK
        if pc == 2:
            showresult(False, pc)  # If false, player lost, then print with bot choice
        else:
            showresult(True, pc)
            wins += 1
    elif usr == 2:  # USER PUTS PAPER
        if pc == 1:
            showresult(True, pc)
            wins += 1
        else:
            showresult(False, pc)
    elif usr == 3: # USER PUTS SCISSORS
        if pc == 1:
            showresult(False, pc)
        else:
            showresult(True, pc)
            wins += 1
    try:
        cont = input("Continue? [S/N] ").strip().upper()
        if cont == "N":
            break
    except KeyboardInterrupt as e:
        print("Usuário AFK")
        break

print("Thank you for playing JOKENPO!")
print("Here are your scores.")
print("-"*30)
print("Statistics".center(30))
print(f"\033[1:30mVictories\033[m:{wins}".center(30))
print(f"Matches played {matches}".center(30))
print(f"\033[4:30mWinrate\033[m: {wins/matches:.2f}".center(30))








