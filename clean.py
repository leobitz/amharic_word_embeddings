import re
import string

lines = open('data/charset.txt', encoding='utf-8').read().split('\n')
am_alphabet = lines[0].strip()
am_digits = lines[1].strip()
am_punc = lines[2].strip()
en_punc = lines[3].strip()
en_digits = string.digits
helper_chars = lines[4].strip()

unk_char = "u"  # unknown word to replace with unknown tokens
unk_word = "unk"

puncs = list(set('()!?#.-"%…/u ' + string.punctuation))
space = '()!?።"፠፡፣፤፥፦፧፨%…'  # characters that should have space around them
space = {c: c for c in space}

max_word_len = 13  # maximum word length

replace_map = open('data/replace.txt', encoding='utf-8').read().split('\n')
replace_map = {line.split('=')[0]: line.split('=')[1]
               for line in replace_map if len(line) > 0}

def _clean_multiple_chars(chars, line):
    patter = re.compile('({0})'.format(chars)+"{2,}")
    line = re.sub(patter, chars, line)
    return line

def clean_text(line):
    for ik, (k, v) in enumerate(replace_map.items()):
        line = line.replace(k, v)
    line = line.strip()  # remove aby trailing spaces around the text
    line = _clean_multiple_chars('"', line)  # replace multiple '"' with single '"' e.g """" => "
    line = _clean_multiple_chars('!', line)  # replace multiple '!' with single '!' e.g !!! => !
    patter = re.compile(r'(\. )')
    # replace multiple '. ' with single '…' e.g . . . . => …
    line = re.sub(patter, '…', line)
    line = re.sub(r'(\.)\1{1,}', "…", line)
    # replace multiple '…' with single '…' e.g …… => …
    line = re.sub(r'\…+', "…", line)
    # replace multiple '… ' with single '… …' e.g … … => …
    line = re.sub(r'\…\s+', "…", line)
    # replace multiple '… ' with single '- -' e.g - - => …
    line = re.sub(r'-+', "-", line)
    # replace multiple '… ' with single '- -' e.g - - => …
    line = re.sub(r'\-\s+', "- ", line)

    new_line = []
    for c in line:
        if c in space:
            # add space around a character if it needs
            new_line.append(" {0} ".format(c))
        else:
            # inset the character without adding space aorund it
            new_line.append(c)
    line = "".join(new_line).strip()
    # finally, replace multiple spaces with a single one
    line = re.sub(r'\s+', " ", line).strip()
    sp = line.split(' ')

    valid_words = []
    # check if every word's length is less than (max_word_len + 1)
    for s in sp:
        if len(s) <= max_word_len:
            valid_words.append(s)
        else:
            valid_words.append(s[:max_word_len])

    line = " ".join(valid_words)
    line = re.sub(f'[^{am_alphabet}{am_digits}{am_punc}{en_digits}{en_punc[:-1]}\- ]', unk_char, line)
    line = re.sub(f"u+\s", f' {unk_word} ', line)
    line = re.sub(r'\s+', " ", line).strip()

    return line
