# amharic word embedding resource
Here you will find resources for amharic word embedding
## Corpus
I have collected a corpus from most of the amharic news websites. After cleaning, the dataset contains around 37.9 million tokens with 1.39 million unique tokens. 

You can find the uncleaned raw dataset here: [Raw Dataset](https://drive.google.com/file/d/1HmsEuNHH0i4GrfSuXqox0FgWMpkQyCMJ/view?usp=sharing)

You can find the cleaned dataset here: [Clean Dataset](https://drive.google.com/file/d/1JTixpw4EvCL9M1FkPA5F4x_Cfhdp67oU/view?usp=sharing)
## Cleaning
I cleaned the dataset using the following procedure. But, you can apply your own on the raw dataset.

* Normalize by replacing characters and words by using the mapping in the [replace](https://github.com/leobitz/amharic_word_embeddings/blob/main/data/replace.txt) file
* Replaced consquative same punctiuations by just one. Example: %%% -> %
* Added spaces around punctiuations. Example: ቻው! -> ቻው !
* Truncated words that have more than 13 charactes to just 13
* Replaced characters other than arabic digits and the charactes in [charset](https://github.com/leobitz/amharic_word_embeddings/blob/main/data/charset.txt) with 'u'. Example: እንሂድxc -> እንሂድuu
* Replaced words that are not amharic with 'unk'. Example: she said ልክ ነው -> unk unk ልክ ነው
* Replaced consquative 'unk' with just one 'unk'. Example: she said ልክ ነው -> unk ልክ ነው
## Alphabezized Word Embeddings

## Embeddings

### FastText
### Alphabetized FastText
### Word2Vec


