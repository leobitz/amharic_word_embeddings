import enum
import re
import string

# load the valid character set that should be in the text
charset = open('data/char-table.txt', encoding='utf-8').read().split('\n')
chars = [line.split(' ') for line in charset]
charset = []
[charset.extend(line) for line in chars]
# split the character sets into individual characters and put them in list
charset.append(' ')
charset = sorted(set(charset))
charset.remove('')

lines = open('data/charset.txt', encoding='utf-8').read().split('\n')
am_alphabet = lines[0].strip()
am_digits = lines[1].strip()
am_punc = lines[2].strip()
en_punc = lines[3].strip()
en_digits = string.digits
helper_chars = lines[4].strip()
# Normalizing map
# character mapping that will be used to map weired (semnatically similar but different unicode chars)
# characters to common, well known semantically similar characters
char_mapping = {
    "(": "[ {".split(' '),  # Exmaple: replace [] by (
    ")": "] }".split(' '),
    '"': "< > 〈 〉《 》 ′ ″ ‶ ‹ › ‘ ’ ‛ “ ”  ፞  ፟ ̋  ̎  ʻ ʼ ʽ ʾ ʿ » ´ « ¨ ` '",
    "፣": '߹ :'.split(),
    '-': '– —— —– —-'.split()
}
# for ik, (k, v) in enumerate(char_mapping.items()):
    
#     for vsx in v:
#         if len(vsx.strip()) != 0:
#             print(vsx + "=" + k)
# character mapping that will be used to string made up of two or more characters
# that were put to signify a single character purpose
reps = {
    # Exmaple: used for mapping ˸˸ => ።
    "።": ":: ∶∶ ：： ᎓᎓ ፡፡ ። ˸˸ ::".split(' '),
    "፦": [':-', ': -', '፡ -', '፡-']
}
# for ik, (k, v) in enumerate(reps.items()):
    
#     for vsx in v:
#         if len(vsx.strip()) != 0:
#             print(vsx + "=" + k)

unk_char = "u"  # unknown word to replace with unknown tokens
reps_map = {}  # reversing the mapping
for key in reps:
    for s in reps[key]:
        reps_map[s] = key

map_char = {}  # reversing the mapping
for key in char_mapping.keys():
    for val in char_mapping[key]:
        map_char[val] = key

puncs = list(set('()!?#.-"%…/u ' + string.punctuation))
space = '()!?።"፠፡፣፤፥፦፧፨%…'  # characters that should have space around them
space = {c: c for c in space}

max_word_len = 13  # maximum word length

replace_map = open('data/replace.txt', encoding='utf-8').read().split('\n')
replace_map = {line.split('=')[0]: line.split('=')[1]
               for line in replace_map if len(line) > 0}


def replace(line, map_char):
    """
    Given a text, it normazlizes by mapping unknown character to their corresponding replacement
    """
    new_chars = []
    for key in reps_map.keys():
        # Example: replace ': -' => '፦' from reps_map
        line = re.sub(key, reps_map[key], line)
    for char in line:
        if char in charset:  # already know charatcer
            new_chars.append(char)
        else:
            if char in map_char:  # character that can be mapped from the normalization made on map_char
                new_chars.append(map_char[char])
            else:
                # if completely unknown character, replaced with <space>
                new_chars.append(unk_char)
    line = " ".join("".join(new_chars).split(" "))
    return line


def clean_multiple_chars(chars, line):
    patter = re.compile('({0})'.format(chars)+"{2,}")
    line = re.sub(patter, chars, line)
    return line


def clean_series_punctuation(line, seq_len=4):
    """
    Given text, it will remove series of unknown tokens if the series has more than 5 tokens

    """
    words = line.split(" ")
    amahric = True
    changed = False
    buffer = []
    main_line = []
    for i in range(len(words)):
        if words[i] in puncs:
            if amahric:
                changed = True
            amahric = False
        else:
            if not amahric:
                changed = True
            amahric = True

        if amahric:
            # print(words[i], amahric, changed)
            if changed:
                if len(buffer) > 5:
                    buffer = [unk_char]
                main_line.extend(buffer)
                buffer = [words[i]]
            else:
                buffer.append(words[i])
        else:

            if changed:
                main_line.extend(buffer)
                buffer = [words[i]]
            else:
                buffer.append(words[i])

        changed = False
        # print(buffer)
    if amahric:
        main_line.extend(buffer)
    else:
        if len(buffer) > 5:
            buffer = [unk_char]
        main_line.extend(buffer)
    text = " ".join(main_line)
    return text


def checkIfAm(text):
    """
    Given a text, returns true if the text contains any amharic letter, punctiuation or digit
    """
    text = set(text)
    for a in text:
        if a in am_alphabet or a in am_digits or a in am_punc:
            return True
    return False


def checkIfFidel(text):
    """
    Given a text, returns true if the text contains only amharic letter or digit
    """
    text = set(text)
    for a in text:
        if a in am_alphabet:
            return True
    return False


def replace_non_am_with_unk(line):
    """
    Given text, it replaces unknown characters with u, otherwise, it will keep a character
    """
    words = line.split(' ')
    new_words = []
    for word in words:
        if checkIfFidel(word):
            new_words.append(word)
        else:
            if len(word) > 1:
                new_words.append(unk_char)
            else:
                new_words.append(word)
    return " ".join(new_words)


def clean_to_text(line):
    for ik, (k, v) in enumerate(replace_map.items()):
        line = line.replace(k, v)
    line = line.strip()  # remove aby trailing spaces around the text
    # if len(line) > 0: # if there are characters
    line = clean_multiple_chars('"', line)  # replace multiple '"' with single '"' e.g """" => "
    line = clean_multiple_chars('!', line)  # replace multiple '!' with single '!' e.g !!! => !
    patter = re.compile(r'(\. )')
    # replace multiple '. ' with single '…' e.g . . . . => …
    line = re.sub(patter, '…', line)
    # patter = re.compile(r'(\.)')
    # line = re.sub(patter, '…', line) # replace multiple '.' with single '…' e.g ... => …
    # patter = re.compile('(#)')
    # replace multiple '#' with single '#' e.g ### => #
    # line = re.sub(patter, '#', line)
    # line = re.sub(r'#+', "#", line)
    # line = re.sub('ዓ.ም.', "ዓ.ም", line)
    line = re.sub(r'(\.)\1{1,}', "…", line)
    # replace multiple '…' with single '…' e.g …… => …
    line = re.sub(r'\…+', "…", line)
    # replace multiple '… ' with single '… …' e.g … … => …
    line = re.sub(r'\…\s+', "…", line)
    # replace multiple '… ' with single '… …' e.g … … => …
    # line = re.sub(r'u+', "u", line)
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
            valid_words.append(unk_char)

    line = " ".join(valid_words)
    line = re.sub(f'[^{am_alphabet}{am_digits}{am_punc}{en_digits}{en_punc[:-1]}\- ]', unk_char, line)
    line = re.sub(f"u+\s", ' unk ', line)
    line = re.sub(r'\s+', " ", line).strip()
    # print(line)
    # line = replace_non_am_with_unk(line)
    return line

# with open('data/clean_corpus.txt', encoding='utf-8', mode='w') as newF:
#     with open('data/corpus.txt', encoding='utf-8', mode='r') as oldF:
#         for line in oldF:
#             line = line.strip()
#             line = clean_to_text(line)
#             newF.write(line)
#             newF.write(' ')


# text = open('data/clean_corpus.txt', encoding='utf-8').read()
# # text = "unk wow unk unk unk wow unk"
# text = 'unk'.join([x for x in text.split('unk') if x.strip() != ''])
# print(len(text.split(' ')))
# open('data/clean_corpus.txt', encoding='utf-8', mode='w').write(text)