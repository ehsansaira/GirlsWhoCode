
def intro():
    print("Hi! Welcome to the chatbox!!")
def process_input(answer):
    if is_valid_input(answer):
        say_greeting()
    else:
        say_default()

    user_input = input()
    if user_input == "yes" or user_input == "maybe":
        say_joke()
    if user_input == "no":
        say_notjoke()
def risingaction():
    print("Ok i am bored now. Let's play a game!")

    user_input = input()
    if user_input == "ok" or user_input == "sure" or user_input == "okay":
        print("yay! Lets play hangman")
        while True:
            play_game()
    else:
        print("Okay I'll just tell more super awesome jokes!")
        if user_input == ("okay") or user_input == "ok" or  user_input == "sure":
            more_jokes()

#DEFINE:

    def say_greeting(word):
        print("what's up! Do you want to hear a joke?")

def is_valid_input(word):
    valid = ["hi", "hey", "hello", "what's up"]
    if word is valid:
        return True
    else:
        return False

def say_default():
    print("very cool. Do you want to hear a joke")
def say_joke():
    print("I’m a big fan of whiteboards. I find them quite re-markable.")
def say_notjoke():
    print("you suck! I'm going to tell you a joke anyway. What did the fish say when he swam into the wall? DAM")
def play_game():
    import random

    potential_words = ["dove", "love", "move", "pineapple", "bottle"]

    word = random.choice(potential_words)

    current_word = []

    for character in word:
        current_word.append("_")
    print(current_word)
    letteroption = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l" "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print(letteroption)

    maxfails = len(word)+3

    fails = 0
    correctguess = 0

    while fails < maxfails:
        guess = input("Guess a letter: ")
        for letters in range (0, len(word)):
            if word[letters] == guess:
                current_word[letters] = guess
                correctguess+=1
        print(current_word)

        fails+=1



        if correctguess == len(word):
            print("You Win!!")
            break
        print("You have " + str(maxfails - fails) + " tries left!")
    if fails == maxfails:
        print("Sorry you lose :( The word is", word)


def more_jokes():
    import random
    potential_jokes = ["Are any Halloween monsters good at math? No- unless you COUNT DRACULA", "Never trust math teachers who use graph paper. They’re always plotting something."]
    word = random.choice(potential_jokes)
    print(word)
# --- Put your main program below! ---

def main():
    intro()
    while True:
      answer = input("(What will you say?)")
      process_input (answer)
      break
    risingaction()
    while True:
        answer = input("(What will you say?)")
        process_input (answer)
        break
    more_jokes()
    while True:
        answer = input("(What will you say?)")
        process_input (answer)
        break
    repeat_or_jokes (answer)
    while True:
        answer = input("(What will you say?)")
        process_input (answer)
        break
if __name__ == "__main__":

  main()
