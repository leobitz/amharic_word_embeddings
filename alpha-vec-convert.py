import nlp_lib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--source', type=str)
parser.add_argument('--map', type=str)
parser.add_argument('--output', type=str)
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
            new_c = tup2char[tup]
            if v == 0:
                chars += [new_c]
            else:
                chars += [new_c, new_v]
        else:
            chars += [char]
    return ''.join(chars)


with open(args.source, encoding='utf-8') as f:
    fline = f.readline().strip().split()
    vocab_size, embed_size = int(fline[0]), int(fline[1])
    abjw2vec = {}
    for line in f:
        line = line.strip().split()
        word, vec = line[0], [float(x) for x in line[1:]]
        word = word.strip()
        abjw2vec[word] = vec

    with open(args.map, encoding='utf-8') as ff:
        line = ff.readline().strip().split()
        vocab_size, embed_size = int(fline[0]), int(fline[1])
        word2word = {}
        for line in ff:
            line = line.strip().split()
            word = line[0]
            word = word.strip()
            word2word[word] = abjw2vec[encode(word)]

    with open(args.output, mode='w', encoding='utf-8') as fg:
        fg.write(" ".join(fline))
        fg.write('\n')
        for word in word2word:
            vec = word2word[word]
            vec = word + " " + " ".join([str(x) for x in vec])
            fg.write(vec)
            fg.write('\n')
