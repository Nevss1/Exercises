from random import randint
score_plr1 = 0
score_plr2 = 0
who_turn = 1


def roll(turn):
    try:
        input(f"player {turn} turn! press any to roll.")
    except KeyboardInterrupt:
        print(" Player AFK")
        return 0
    score_sum = 0
    while True:
        score = randint(0, 6)  # pontuação do dado de seis lados
        if score == 1:
            print("Pig!")
            return 0
        else:
            print(f"You score {score}!")
            score_sum += score
            try:
                can_roll = input("Press any to roll (h to hold) ")
                if can_roll == "h":
                    print(f"You scored {score_sum} points!")
                    return score_sum
                else:
                    continue
            except KeyboardInterrupt:
                print(" Player AFK")


'''
Gameplay PIG dice game:
Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":

    If the player rolls a 1, they score nothing and it becomes the next player's turn.
    If the player rolls any other number, it is added to their turn total and the player's turn continues.
    If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
'''

while True:
    if who_turn == 1:
        score_plr1 += roll(who_turn)  # turno do player1
        print(f"Player {who_turn} total points: {score_plr1}")
        if score_plr1 >= 100:
            print("Congrats!! Player 1 won the PIG game!")
            break
        who_turn = 2  # troca de player
    elif who_turn == 2:
        score_plr2 += roll(who_turn) # turno do player 2
        print(f"Player {who_turn} total points: {score_plr2}")
        if score_plr2 >= 100:
            print("Congrats!! Player 1 won the PIG game!")
        who_turn = 1




    """if turn == "plr1":
        can_roll = input(f"player {points_plr1} turn! press any to roll.")
        score = roll()
        if score == 1:
            turn = 1
            continue
        else:
            score_sum += score
            can_roll = input("Wanna roll again or hold? (r, h) ")
            if can_roll == "r":
                pass
            elif can_roll == "h":
                pass
            else:"""




