import random

class GameManager:
    """Is responsible for the guessing assepct of the game and selecting a random word, processing guesses, and returning what will be printed to the terminal

        Attributes: 
            -random_word = The random word taken from a list of words.
            -_word_list(list) = List of words to be used
            -letters_guessed(string) = what letters have been guessed.
            -letters_left(int) = How many letters remain in the word.
            -turn_number(int) = How many wrong guesses remain in the game.
    
    """
    def __init__(self):
        """Constructs a new GameManager.

        Args:
            self (GameManager): an instance of GameManager.
        """
        self._random_word = ""
        self._word_list = {}
        self._rand = 0
        self._letters_guessed = ""
        self.letters_left = 0
        self.turn_number = 6
        self._print = ""
        self.final__print = ""

    def word(self):
        """Generates a random word.
        
        Args:
            self (GameManager): an instance of GameManager.
        """
        self._word_list = {
            0: 'football',
            1: 'basketball',
            2: 'baseball',
            3: 'volleyball',
            4: 'pickleball'
        }
        self._rand = random.randint(0, 4)
        self._random_word = self._word_list[self._rand]

    def check_letter(self, guess):
        """Shows hints to the user
        
        Args:
            self (GameManager): an instance of GameManager.
        """
        if guess in self._random_word:
            self._print = "Correct!"
        else:
            self.turn_number -= 1
            self._print = (f"Incorrect. There are no {guess} in the secret word. {self.turn_number} turn(s) left.")
        
        return self.turn_number

    def _turn_count(self, guess):
        """Keeps count of incorrect guesses.

        Args:
            self (GameManager): an instance of GameManager.
        """
        self._letters_guessed += guess
        self.letters_left = 0
        for letter in self._random_word:
            if letter in self._letters_guessed:
                print(f"{letter}", end="")
            else:
                print("_ ", end="")
                self.letters_left += 1
        return self.letters_left

    def _game_won(self, letters_left, turn_number):
        """Checks to see if the game is finished.

        Args:
            self (GameManager): an instance of GameManager.
        """
        
        if letters_left == 0:
            self.final_print = (f"Congratulations! The secret word was: {self._random_word}. You win!")
            return True

        if turn_number == 0: 
            self.final_print = (f"Sorry you lost")
            return True
