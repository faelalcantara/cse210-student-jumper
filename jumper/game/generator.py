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
    self.current_word = ''
    self.word_letters = []
    self.importer = Importer()

  def read_external_file(self, filename):
    # Reads an external file and imports it as a list of words. This is very standard python code from CSE 111
    word_list = []
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            word_list.append(clean_line)
    # print(word_list)
    return word_list

  def import_words(self):
    try:
      # Tries to import the wordlist of 10000 entries from the external file. It it success, it will replace the basic `self.words` list
      impoted_words = self.read_external_file("jumper/game/wordlist10000.txt")
      # Only allows words with 4 or more characters into the game
      words_filtered_by_length = [word for word in impoted_words if len(word) >= 4]
      self.words = words_filtered_by_length
      # If this fails, the game will continue with the basic `self.words` list 
    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")

  def generate_word(self):
    # By calling this method, the basic 3 word list gets replaced with thousands of words from the external file
    self.importer.import_words()

    # Generates the word random
    word_index = random.randint(1, len(self.words))
    self.current_word = self.words[word_index - 1]
    self.split_word()

    # For testing:
    # print(self.current_word)

  def split_word(self):
    # Separates each letter in saving in a list
    word = self.current_word
    for i in range(len(word)):
      self.word_letters.append(word[i])

  def check_characters(self, character) -> bool:
    # Simply acts as a filter to check if the character entered by the player is an actual letter in the English alphabet
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)

    if character in alphabet_list:
      return True
    else:
      return False
