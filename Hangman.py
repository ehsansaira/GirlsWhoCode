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
