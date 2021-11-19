import clean
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_path", type=str)
parser.add_argument("-o", "--output_path", type=str)
parser.add_argument("-l", "--max_word_length", type=int, default=13)
args = parser.parse_args()
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit()

input_file = args.input_path
output_file = args.output_path
max_word_length = args.max_word_length

with open(output_file, encoding='utf-8', mode='w') as newF:
    with open(input_file, encoding='utf-8', mode='r') as oldF:
        for line in oldF:
            line = line.strip()
            line = clean.clean_text(line)
            # replace continous unk with a single one. Example unk unk unk => unk
            line = 'unk'.join([x for x in line.split(clean.unk_word) if x.strip() != ''])
            newF.write(line)
            newF.write(' ') # replace with \n if you want it to write in new lines