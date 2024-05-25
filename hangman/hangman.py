import random
import time

hangman_data = ["banana", "computer", "elephant", "sunshine", "happiness", "butterfly", "chocolate", "rainbow", "universe",
                "adventure", "pencil", "diamond", "mountain", "guitar", "pizza", "dragon", "waterfall", "football", "telescope", "moonlight",
                "jellyfish", "fireworks", "elephant", "cupcake", "starfish", "strawberry", "snowflake", "cucumber", "parrot", "pineapple",
                "beach", "castle", "firefly", "basketball", "elephant", "kangaroo", "lighthouse", "watermelon", "trampoline", "zebra", "giraffe",
                "treasure", "rainbow", "bubblegum", "dragonfly", "umbrella", "cookie", "ocean", "lion", "horse", "cupboard", "penguin", "coconut",
                "telescope", "octopus", "volcano", "kangaroo", "popcorn", "unicorn", "sandcastle", "carousel", "spaceship", "telephone",
                "caterpillar", "waterfall", "keyboard", "seashell", "orchestra", "elephant", "basketball", "pineapple", "iceberg", "telescope",
                "elephant", "butterfly", "rainbow", "moonlight", "chocolate", "ice cream", "aeroplane", "guitar", "starfish", "jellyfish", "snowman",
                "cupcake", "elephant", "watermelon", "treasure", "parrot", "rainbow", "waterfall", "butterfly", "dragonfly", "sandcastle", "lighthouse",
                "carousel", "chocolate", "basketball", "adventure", "universe, cigarette, queen, problem, spotlight, apple"]

word = random.choice(hangman_data)  # choose a random word
guessed_word = ["_" for _ in word]
strikes = 0
guessed_letters = []

print(" ".join(guessed_word))  # print initial state

while "_" in guessed_word:  # check if the word is unguessed
    guess = input("Guess a letter: ").lower()  # guess a letter

    if len(guess) != 1 or not guess.isalpha():  # check if the length is one or whether it is alphabetic
        print("Please enter a single letter.")  # error message
        print()
        continue
    if guess in guessed_letters:
    	print("You already guessed this letter!")
        print()
    	continue

    if guess in word: #check if the guess is inside our original word
        for i in range(len(word)): #check over the word
            if word[i] == guess: #check for every character
                guessed_word[i] = guess #change the "_" to the guessed letter
                guessed_letters.append(guess) #add guess to guessed letters!
        print(" ".join(guessed_word)) #print the word again
        print()
    else:
        strikes += 1 #add a point to the number of strikes
        print(f"Incorrect guess. Your number of strikes is now {strikes}")
        print()


print(f"Congrats you guessed the word!!! It took you {strikes} strikes.")
time.sleep(3)