from utils import load_all_rhyming_syllables, rhyme_to_list, get_last_word


class Rhymer():
    def __init__(self):
        # Load the word to last rhyming syllable mapping in memory
        self.word_syllable_map = load_all_rhyming_syllables()


    def pre_process_rhymes(self, rhyme_lines):
        # To remember the order of the last words in each line of each rhyme
        last_words_in_rhymes = []
        # Get the last words, syllables for all the lines in all the rhymes
        # This is the master dictionary that is prepared for the actual operations
        words_to_check = {}
        for rhyme in rhyme_lines:
            last_words_in_rhyme = []
            # Go through each line of the rhyme
            for line in rhyme:
                # Get the last word in each line
                last_word = get_last_word(line)
                # Store it in a list to maintain the order in which the words occured
                last_words_in_rhyme.append(last_word)
                # Go to the heavy dictionary only if the word is not already loaded
                if last_word not in words_to_check:
                    words_to_check[last_word] = self.word_syllable_map[last_word]
            last_words_in_rhymes.append(last_words_in_rhyme)
        return last_words_in_rhymes, words_to_check

    def break_rhymes_into_lines(self, rhymes):
        rv = []
        for rhyme in rhymes:
            rv.append(rhyme_to_list(rhyme))
        return rv

    def get_rhyming_scheme(self, rhymes):
        # Find the rhyming scheme
        rhyme_lines = self.break_rhymes_into_lines(rhymes)
        last_words_in_rhymes, words_to_check = self.pre_process_rhymes(rhyme_lines)
        for rhyme_counter, rhyme_words in enumerate(last_words_in_rhymes):
            counter = 1
            covered_syllables = {}
            for line_counter, word in enumerate(rhyme_words):
                # print word, words_to_check[word]
                syllable_value = ''
                for item in words_to_check[word]:
                    if item not in covered_syllables:
                        covered_syllables[item] = counter
                    if not syllable_value:
                        syllable_value = covered_syllables[item]
                print rhyme_lines[rhyme_counter][line_counter], syllable_value
                counter += 1
