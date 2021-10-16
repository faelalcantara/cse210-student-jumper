import random
import string

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

  def read_external_file(self, filename):
    word_list = []
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            word_list.append(clean_line)

    print(word_list)
    return word_list

  def import_words(self):
    # try:
      self.read_external_file("wordlist10000.txt")
    # except (FileNotFoundError, PermissionError) as error:
    #     print(type(error).__name__, error, sep=": ")

  def generate_word(self):
    # Generates the word random

    self.import_words()

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
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)

    if character in alphabet_list:
      return True
    else:
      return False
