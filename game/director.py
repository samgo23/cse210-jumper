from game.terminal_service import TerminalService
from game.game_manager import GameManager
from game.jumper import Jumper

class Director: 
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        jumper (Jumper): The game's jumper.
        is_playing (boolean): Whether or not to keep playing.
        _game_manger (GameManager): The games manager
        terminal_service: For getting and displaying information on the terminal.
    """
    
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._terminal_service = TerminalService()
        self._game_manager = GameManager()
        self._jumper = Jumper()
        self.guess = ""
        self.letter = ""
        self.turn_number = 6

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._game_manager.word()

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

            if self._game_manager._game_won(self.letter, self.turn_number) == True:
                self._terminal_service.write_text(self._game_manager.final_print)
                self._is_playing = False

    
    def _get_inputs(self):
        """Generates a random word, prompts user to guess a letter.

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text('')
        self.guess = self._terminal_service.read_text("Enter a letter: ")
        self.turn_number = self._game_manager.check_letter(self.guess)
        self._terminal_service.write_text(self._game_manager.print)
        self._terminal_service.write_text('')
        


    def _do_updates(self):
        """Checks if letter is correct.

        Args:
            self (Director): An instance of Director.
        """
        self.letter = self._game_manager._turn_count(self.guess)
        self._terminal_service.write_text('')
        
        

    def _do_outputs(self):
        """Updates parachute and word, check if the game is finished.

        Args:
            self(Director): an instance of Director.
        
        """
        self._terminal_service.write_text('')
        
        self._terminal_service.write_text(self._jumper.draw_jumper()[self.turn_number])

        self._terminal_service.write_text('')
        
