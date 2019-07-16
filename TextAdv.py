
start = '''
print("You're standing at the entrance of a maze and you have 30 minutes to find your way out.")"
'''

print("start")

print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
user_input = input()
if user_input == "left":
    print("You decide to go left and get a fireball thrown at you. you die.") # Update to match your story.
    # Continue code to finish story.
elif user_input == "right":
    print("You choose to go right and there are two different pathways.")
    print("Type 'left' to go left or 'right' to go right")

    user_input = input()
    if user_input == "right":
        print("A giant shark attacks from an underground pond. You escape quickly but lose an arm. You can no longer continue.")

    elif user_input == "left":
        print ("A clear, beautiful pathway lay ahead. Continue for one mile until reaching your next intersection")
        print("The clock is ticknig. The next intersection approaches. You can go down the ladder, into the lagoon. You can go straight to walk across the unstable bridge. Type 'down' to go down or 'straight' to go straight.")

        user_input = input()
        if user_input == "down":
            print("Congratulations! You are swimming in the lagoon with wonerous sea creatures! They take you to the end of the maze and you are congratulated.")

        elif user_input == "straight":

            print("Uh oh... that was a bumpy ride. You almost didn't make it! The finish line is near! You can continue through the dark woods on foot. Or, steal a struck you see in the distance. Type 'truck' to steal the truck or 'foot' to continue.")

            user_input = input()
            if user_input == "truck":
                print("You find the kepys outside of the truck and sped through the woods. THe truck broke down halfway through the forest, but you remained hopeful because you saw the finish line. Congratulations, you made it!")
            elif user_input == "foot":
                print("Risky choice, sir. You heard sudden noises every step of the way. There were bugs biting you, you stepped on a frong, and a jaguar almost attacked you. Nonetheless, you made it, FIVE MINUTES LATE! All of your belongings have been stripped from you :( Better luck next time!")
