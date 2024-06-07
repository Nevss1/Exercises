def new_game():
    guesses_wrong = []  # list of al guesses
    guess_temp = list()  # guess used for temporarily
    print("Let's start the quiz game!")
    count = 0
    for k, v in questions.items():
        for i in range(0, 3):
            print(options[count][i])
        choice = input("What is your choice? ").upper().strip()
        while True:
            if choice != v and choice in "ABC":
                print("\033[0:31mWrong!\033[m Try Again")
                guess_temp.append(choice)
                choice = input("What is your choice? ").upper().strip()
                print(choice)
            elif choice not in "ABC":
                print("Invalid argument! Please Try again.")
                choice = input("What is your choice? ").upper().strip()
            else:
                print("\033[0:32mCorrect!\033[m")
                break
        guesses_wrong.append(guess_temp[:])
        guess_temp.clear()
        count += 1
    print("Your guesses:")
    for v in guesses_wrong:
        print(v)


questions = {
    "When was WWII started?": 'C',
    "Who was Getúlio Vargas?": "A",
    "Where is México?": "B"
}
options = [["A. March 3rd, 1936", "B. February 15, 1935 ", "C. September 1st 1936"],
           ["A. Politic", "B. Cooker", "C. Mechanic"],
           ["A. In Africa", "B. In North America", "C. In Asia"]]

new_game()
