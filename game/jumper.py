class Jumper:
    """Jumper is responsible for drawing the jumper in the terminal 

      Attributes:
        jumper (dictionary): contains the jumper output.
    """

    def __init__(self):
        """Contruncts a new Jumper.

        Args:
          self (Jumper): An instance of Jumper.
        
        """
        self.jumper = {}

    def draw_jumper(self):
        """Draws the jumper.
        
          Args:
            Self (Jumper): An instance of Jumper.
        """
        self.jumper ={
          6:"  ___\n /___\\\n \   /\n  \ /\n   O\n  /|\\\n  / \\\n^^^^^^^^",
          5:" /___\\\n \   /\n  \ /\n   O\n  /|\\\n  / \\\n^^^^^^^^",
          4:"  ___ \n \   /\n  \ /\n   O\n  /|\\\n  / \\\n^^^^^^^^",
          3:" \   /\n  \ /\n   O\n  /|\\\n  / \\\n^^^^^^^^",
          2:"  \ /\n   O\n  /|\\\n  / \\\n^^^^^^^^",
          1:"   O\n  /|\\\n  / \\\n^^^^^^^^",
          0:"   x\n  /|\\\n  / \\\n^^^^^^^^",
        }
        return self.jumper

