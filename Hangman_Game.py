import random

# List of words with descriptions (word, description)
words = [
    ("python", "A popular programming language known for its simplicity."),
    ("arduino", "An open-source electronics platform based on easy-to-use hardware and software."),
    ("internet", "A global network providing communication and information exchange."),
    ("keyboard", "An input device used to type text into computers."),
    ("robot", "A machine capable of carrying out a complex series of actions automatically."),
    ("sensor", "A device that detects changes in the environment and sends information to other devices."),
    ("algorithm", "A process or set of rules followed in calculations or problem-solving operations."),
    ("database", "A structured set of data held in a computer, especially one that is accessible in various ways."),
    ("computer", "An electronic device that processes data and performs tasks according to instructions."),
    ("satellite", "A man-made object placed in orbit around the earth or another planet to collect information or for communication.")
]

# Function to randomly reveal two letters in the word
def reveal_two_letters(word, guessed_word):
    indices = random.sample(range(len(word)), 2)  # Pick two random indices
    for index in indices:
        guessed_word[index] = word[index]  # Reveal the letter at the random index
    return guessed_word

# Function to play Hangman
def play_hangman():
    word, description = random.choice(words)  # Randomly select a word and description
    word_length = len(word)
    attempts = word_length * 2  # Maximum attempts is twice the word length
    guessed_word = ["_"] * word_length  # Placeholder for the guessed word
    
    # Reveal two random letters
    guessed_word = reveal_two_letters(word, guessed_word)
    
    guessed_letters = []  # List to store all guessed letters (correct and incorrect)
    correct_guessed_letters = []  # List to store only correct guessed letters
    
    print("Welcome to Hangman!")
    print(f"Hint: {description}")
    print(" ".join(guessed_word))
    
    while attempts > 0:
        guess = input(f"\nYou have {attempts} attempts left. Guess a letter: ").lower()
        
        # If the letter was already guessed
        if guess in guessed_letters:
            if guess in correct_guessed_letters:
                print(f"You've already correctly guessed the letter '{guess}', try a different one.")
            else:
                print(f"You've already guessed the letter '{guess}', and it was incorrect. Try a different one.")
            continue
        
        # Add the letter to guessed letters
        guessed_letters.append(guess)
        
        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            correct_guessed_letters.append(guess)  # Add to correct guesses
            
            for i in range(word_length):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
            attempts -= 1  # Reduce attempts for incorrect guess
        
        print(" ".join(guessed_word))
        
        # Check if the player has guessed the word
        if "_" not in guessed_word:
            print(f"\nCongratulations! You guessed the word '{word}' correctly!")
            break
    else:
        print(f"\nYou're out of attempts! The word was '{word}'.")

# Start the game
if __name__ == "__main__":
    play_hangman()
