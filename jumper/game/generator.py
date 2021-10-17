import random
import string
from game.importer import Importer

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
    self.importer = Importer()

  def generate_word(self):
    # By calling this method, the basic 3 word list gets replaced with thousands of words from the external file
    self.words = self.importer.import_words()

    # Generates the word random
    word_index = random.randint(1, len(self.words))
    current_word = self.words[word_index - 1]
    word_letters_list = self.split_word(current_word)
  
    # For testing:
    # print(self.current_word)
    return word_letters_list

  def split_word(self, word):
    # Separates each letter in saving in a list
    word_letters_list = []
    for i in range(len(word)):
      word_letters_list.append(word[i])
    
    return word_letters_list

  def check_characters(self, character) -> bool:
    # Simply acts as a filter to check if the character entered by the player is an actual letter in the English alphabet
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)

    if character in alphabet_list:
      return True
    else:
      return False
