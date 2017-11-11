import nltk
from nltk.corpus import cmudict
from example import examples
import string
from nltk.tokenize import word_tokenize


def load_all_rhyming_syllables():
    word_syllable_map = {}
    for cmutuple in cmudict.entries():
        syllables = cmutuple[1]
        rep = ''
        for index, syllable in enumerate(syllables[-1::-1]):
            if syllable[-1] in ['1', '2']:
                rep = ' '.join(syllable[index:])
                break
        if rep:
            if cmutuple[0] in word_syllable_map:
                word_syllable_map[cmutuple[0]].append(rep)
            else:
                word_syllable_map[cmutuple[0]] = [rep]
    return word_syllable_map


def remove_whitespace(text):
    return text.strip().replace('\t', '').replace('\r', '')


def remove_punctuation(text):
    return text.translate(None, string.punctuation)


def remove_unnecessary_characters(text, whitespace):
    return remove_punctuation(remove_whitespace(text)) \
            if whitespace \
            else remove_punctuation(text)


def rhyme_to_list(rhyme, whitespace=False):
    return [
        remove_unnecessary_characters(a, whitespace)
        for a in rhyme.split('\n')
        if remove_unnecessary_characters(a, whitespace)
    ]


def get_last_word(line):
    return word_tokenize(line)[-1]
