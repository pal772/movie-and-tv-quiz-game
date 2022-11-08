def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print(".....................")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D: ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(question.get(key), guess)
        question_num += 1

# --------------------------        
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


# --------------------------
def display_score():
    pass
# --------------------------
def play_again():
    pass


questions = { 
    "What is the name of the song that Queen Elsa sings as she builds her ice castle in the frozen movie?: ": "A",
    "How many films did Sean Connery play James Bond?: ": "C",
    "Which Indiana Jones movie was released back in 1984?: ": "D",
    "How many Lord of the Rings films are there?: ": "A",
    "What was the name of the actor who plays Jack Dawson in Titanic?: ": "B"
}

options = [["A. Let It Go", "B. Circle of Life", "C. Once Upon a Dream", "D. A Whole New World"],
          ["A. Three", "B. Five", "C. Seven", "D. Eight"],
          ["A. Raiders of the Lost ark", "B. The Lost City", "C. The Mosquito Coast", "D. Temple of Doom"],
          ["A. Three", "B. Two", "C. Four", "D. Five"],
          ["A. Brad Pitt", "B. Leonardo DiCaprio", "C. Orlando Bloom", "D. Hugh Dancy"]]