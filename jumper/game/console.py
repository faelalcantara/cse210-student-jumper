from game.generator import Generator

class Console:
  """A code template for a console that will display all information on screen. The responsibility of this 
    class of objects is to privide all the game interactions, keep track of the values, the score 
    and determine if the player win or lose.

  Attributes:
    user input: A string with the letter it choosed
    illustration: A list with the illustration of a skydiver
    generator: An instance of the cass Generator
    word letters: A list with the letters of the generated word
    hidden letters: A list of dashes to be replacede with the letters of the word
  """

  def __init__(self):
      """Class constructor. Declares and initializes instance attributes.

      Args:
        self (Console): An instance of Console.
      """
      self.user_input = ''
      self.illustration = [
          "  ___  ",
          " /___\ ",
          " \   / ",
          "  \ /  ",
          "   0   ",
          "  /|\  ",
          "  / \  "]
      self.generator = Generator()
      
  def ask(self):
      # Asks the user for a word and saves it in the variable.
      answer = input("Guess a letter [a-z]: ")
      answer = answer.strip().lower()

      # Checks whether the input is an actual a-z character
      is_valid = self.generator.check_characters(answer)
      if is_valid:
        self.user_input = answer[0]
      else:
        # Maybe the player can be penalised for not addid valid characters
        print("Sorry, that's not a valid character!")

  def show_illustration(self):
      # Displays the skydiver illustration
      print()
      for i in range(len(self.illustration)):
          print(self.illustration[i])

      print("\n^^^^^^^")

  def play(self, word_letters):
      """Starts the game initializing the word generator, creating a list with only dashes to be
        replaced later with the letters when the player guess it. Keep track of how many chances the
        player still have. Determines if the player win or not.
      """
      hidden_letters = []

      print("\n--------- JUMPER GAME ---------")

      # Creates a list with dashes to be replaced later
      for i in range(len(word_letters)):
          hidden_letters.append('_')

      # Checks if the player can play based on the parachute
      # While parachute is not gone the player can play
      while len(self.illustration) > 3:
          print()
          word = ' '.join(hidden_letters)
          print(word)

          self.show_illustration()
          print()

          # Checks if the player won the game
          if word_letters == hidden_letters:
              print("\n------ YOU WON THE GAME -------")
              print("---------- GOOD JOB -----------")
              quit()
          else:
              self.ask()

          # Checks if the player guessed the letter
          if self.user_input in word_letters:
              for i in range(len(word_letters)):
                  if self.user_input == word_letters[i]:
                      hidden_letters[i] = self.user_input
          else:
              self.illustration.pop(0)

      # Checks if the player lost the game
      if len(self.illustration) == 3:
          self.illustration[0] = '   X   '
          self.show_illustration()
          print("\n---------- GAME OVER ----------")
