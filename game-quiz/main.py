

def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)
    play_again()

def check_answer(correctAnswer, guess):
    if correctAnswer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses, guesses):
    print("-----------------------------")
    print("RESULTS")
    print("-----------------------------")
    print("Total score: " + str(correct_guesses) + "/" + str(len(questions)))
    print("-----------------------------")
    for i in guesses:
        print(i)
    print("-----------------------------")

def play_again():
    response = input("Do you want to play again? (y/N): ").upper()
    if response in ["Y", "y"]:
        new_game()

questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A",
    "Is the sky blue?: ": "A",
}

options = [
    ["A. Guido van Rossum", "B. Elton John", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1945", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. Yes", "B. No"],
    ["A. Yes", "B. No"],
]

new_game()