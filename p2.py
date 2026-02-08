import random

# ----- Word list (small on purpose) -----
WORDS = [
    "crane", "trace", "slate", "flame", "blame",
    "grape", "plane", "brick", "pride", "shine",
    "stone", "money", "cigar", "reign", "sweet",
    "sound", "round", "heart", "earth", "water"
]


# ----- Core scoring logic -----
def score_guess(guess, secret):
    correct_letters = []
    for i in range(len(secret)):
            if guess[i] == secret[i]:
                correct_letters.append("Y")
            elif guess[i] in secret:
                correct_letters.append("O")
            else:
                correct_letters.append("X")

    return "".join(correct_letters)


# ----- Check guess formatting -----
def is_valid_guess(guess):
    return guess.islower() and len(guess) == 5 and guess.isalpha()

# ----- Choose secret word -----
def choose_secret(words):
   return words[0]





# ----- One turn of the game -----
def play_turn(secret, guess):
    if len(guess) == 5 and guess == guess.lower():
        return score_guess(guess , secret)
    else:
         return "Invalid guess"


# ----- Full Wordle game -----
def play_game(words):
    secret = choose_secret(words)

    for i in range(5):

        guess = input("What is your guess? ")
        x = play_turn(secret , guess)

        if x == "YYYYY":
            print("YOU WIN!")
            break

        print(x)
    print("Loser!!!!")


