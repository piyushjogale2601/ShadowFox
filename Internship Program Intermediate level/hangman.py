import random
words = ["apple", "banana", "cherry", "orange", "grape", "lemon", "melon", "pear"]

def choose_word(words):
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def display_hangman(incorrect_guesses):
    hangman_art = [
        """
         ____ 
        |    |
        |    
        |    
        |     
    ____|____
        """,
        """
          ____ 
        |    |
        |    O
        |    
        |     
    ____|____
        """,
        """
          ____ 
        |    |
        |    O
        |    |
        |     
    ____|____
        """,
        """
          ____ 
        |    |
        |    O
        |   /|
        |     
    ____|____
        """,
        """
         ____ 
        |    |
        |    O
        |   /|\  
        |     
    ____|____
        """,
        """
         ____ 
        |    |
        |    O
        |   /|\ 
        |   /  
    ____|____
        """,
        """
         ____ 
        |    |
        |    O
        |   /|\ 
        |   / \ 
    ____|____
        """
    ]
    print(hangman_art[incorrect_guesses])

def hangman_game():
    print("Welcome to Hangman!")
    
    word = choose_word(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6 
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord:", display_word(word, guessed_letters))
        display_hangman(incorrect_guesses)
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word:
            incorrect_guesses += 1
        
        if incorrect_guesses == max_incorrect_guesses:
            display_hangman(incorrect_guesses)  
            print("\nThe word was:", word)
            print("Game Over! You lose.")
            break
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman_game()

hangman_game()
