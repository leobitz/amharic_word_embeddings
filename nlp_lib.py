
def is_all_am_alphabet(text, am_alphabet):
    """
    Given a text, returns true if the text contains only amharic letters
    """
    text = set(text)
    for a in text:
        if a in am_alphabet:
            return True
    return False

def build_charset(charset_file):
    """
    returns charcter mapping to integer and vice versa

    """
    charset = open(charset_file, encoding='utf-8').readlines()
    n_consonant = len(charset)
    n_vowel = 0
    char2int, int2char, char2tup, tup2char = {}, {}, {}, {}
    j = 0
    for k in range(len(charset)):
        row = charset[k][:-1].split(' ')
        if len(row) > n_vowel:
            n_vowel = len(row)
        for i in range(len(row)):
            char2tup[row[i]] = (k, i)
            int2char[j] = row[i]
            char2int[row[i]] = j
            tup = "{0}-{1}".format(k, i)
            tup2char[tup] = row[i]
            j += 1
    return char2int, int2char, char2tup, tup2char, n_consonant, n_vowel
