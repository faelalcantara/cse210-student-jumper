import random

class Generator:
  """A code template for a generetor that will generate random words. The responsibility of this 
    class of objects is to privide random words for the game.
    
  Attributes:
    words: A list of words
    current_word: A word that has been chosen at random
    word letters: The letters of the chosen word separated as a list
  """

  def __init__(self):
    """Class constructor. Declares and initializes instance attributes.

    Args:
      self (Generator): An instance of Generator.
    """
    self.words = ['yellow', 'person', 'motorcycle']
    self.current_word = ''
    self.word_letters = []

  def generate_word(self):
    # Generates the word random
    word_index = random.randint(1, len(self.words))
    self.current_word = self.words[word_index - 1]
    self.split_word()

  def split_word(self):
    # Separates each letter in saving in a list
    word = self.current_word
    for i in range(len(word)):
      self.word_letters.append(word[i])
