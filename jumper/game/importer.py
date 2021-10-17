
class Importer:

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
