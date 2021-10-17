from game.generator import Generator
from game.console import Console

class Director:

    def __init__(self):
        self.generator = Generator()
        self.console = Console()

    def start_callings(self):
        
        word_letters_list = self.generator.generate_word()
        self.console.play(word_letters_list)
