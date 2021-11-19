from lib import *
import argparse
import nlp_lib

parser = argparse.ArgumentParser()
parser.add_argument('--input_file', type=str)
parser.add_argument('--output_file', type=str)
args = parser.parse_args()

char2int, int2char, char2tup, tup2char, n_consonant, n_vowel = nlp_lib.build_charset("data/char-table.txt")
vowels = ['e', 'u', 'i', 'a', 'ê', 'æ', 'o', 'õ', 'ø', 'ü', 'ç', 'ð']
lines = open('data/charset.txt', encoding='utf-8').read().split('\n')
am_alphabet = lines[0].strip()

def encode(word):
    chars = []
    if not nlp_lib.is_all_am_alphabet(word, am_alphabet):
        return word
    for char in word:
        if char in am_alphabet:
            c, v = char2tup[char]
            new_v = vowels[v]
            tup = "{0}-0".format(c)
            # if tup not in tup2char:
            #     tup = "{0}-0".format(c)
            new_c = tup2char[tup]
            if v == 0:
                chars += [new_c]
            else:
                chars += [new_c, new_v]
        else:
            chars += [char]
    return ''.join(chars)


lines = open(args.input_file, encoding='utf-8').read().split('\n')
abj_file = open(args.output_file, encoding='utf-8', mode='w')
for line in lines:
    words = line.split(' ')
    abj_words = []
    for word in words:
        abj = encode(word)
        abj_words.append(abj)
    abj_line =" ".join(abj_words)
    abj_file.write(abj_line)
    abj_file.write("\n")
abj_file.close()