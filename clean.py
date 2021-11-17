import re
import string

lines = open('data/charset.txt', encoding='utf-8').read().split('\n')
am_alphabet = lines[0]
am_digits = lines[1]
am_punc = lines[2]
# Normalizing map
# character mapping that will be used to map weired (semnatically similar but different unicode chars)
# characters to common, well known semantically similar characters
char_mapping = {
    "(": "[ {".split(' '), # Exmaple: replace [] by (
    ")": "] }".split(' '),
    '"':"< >〈 〉 《 》 ′ ″ ‶ ‹ › ‘ ’ ‛ “ ”  ፞  ፟ ̋  ̎  ʻ ʼ ʽ ʾ ʿ » ´ « ¨ ` '".split(' '),
    "#": '0 1 2 3 4 5 6 7 8 9'.split(' '),
    "፣": '߹ :',
    " ": ' ',
    '-': '– —— —– —-'
}
# character mapping that will be used to string made up of two or more characters
# that were put to signify a single character purpose
reps = {
    "።": ":: ∶∶ ：： ᎓᎓ ፡፡ ። ˸˸ ::".split(' '), # Exmaple: used for mapping ˸˸ => ።
    "፦": [':-', ': -', '፡ -', '፡-']
}

unk_char = "u" # unknown word to replace with unknown tokens
reps_map ={} # reversing the mapping
for key in reps:
    for s in reps[key]:
        reps_map[s] = key

map_char = {} # reversing the mapping
for key in char_mapping.keys():
    for val in char_mapping[key]:
        map_char[val] = key

puncs = list(set('()!?#.-"%…/u ' + string.punctuation))
space = '()!?።"፠፡፣፤፥፦፧፨%…' # characters that should have space around them
space = {c:c for c in space}

max_word_len  = 13 # maximum word length
