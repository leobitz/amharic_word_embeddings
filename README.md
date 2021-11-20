# amharic word embedding resources
Here you will find resources for amharic word embedding
## Corpus
I have collected a corpus from most of the amharic news websites. After cleaning, the dataset contains around 37.9 million tokens with 1.39 million unique tokens. 

You can find the uncleaned raw dataset here: [Raw Dataset](https://drive.google.com/file/d/1HmsEuNHH0i4GrfSuXqox0FgWMpkQyCMJ/view?usp=sharing)

You can find the cleaned dataset here: [Clean Dataset](https://drive.google.com/file/d/1JTixpw4EvCL9M1FkPA5F4x_Cfhdp67oU/view?usp=sharing)
## Cleaning
I cleaned the dataset using the following procedure. But, you can apply your own on the raw dataset.

* Normalize by replacing characters and words by using the mapping in the [replace](https://github.com/leobitz/amharic_word_embeddings/blob/main/data/replace.txt) file
* Replaced consecutive same punctuations by just one. Example: %%% -> %
* Added spaces around punctuations. Example: ቻው! -> ቻው !
* Truncated words that have more than 13 characters to just 13
* Replaced characters other than arabic digits and the characters in [charset](https://github.com/leobitz/amharic_word_embeddings/blob/main/data/charset.txt) with 'u'. Example: እንሂድxc -> እንሂድuu
* Replaced words that are not amharic with 'unk'. Example: she said ልክ ነው -> unk unk ልክ ነው
* Replaced consecutive 'unk' with just one 'unk'. Example: she said ልክ ነው -> unk ልክ ነው
## Alphabetized Word Embeddings
Please read our paper to understand why Alphabetized word embedding is better than the normal fasttext word embeddings. In short, it unravels the syntactic information between characters. That simply allows the fasttext algorithm to learn better embeddings that captures syntactic information. 

Example of alphabetization: ትሄዳለች -> ተæሀêደaለቸæ

To convert an amharic text file to alphabetized one, use [this script](https://github.com/leobitz/amharic_word_embeddings/blob/main/alphabetizor.py)
## Amharic Word Analogy
In our study, we collected an amharic word analogy test. You can find it [here](https://github.com/leobitz/amharic_word_embeddings/blob/main/eval/word-analogy.txt). If you need the alphabetized version, find it [here](https://github.com/leobitz/amharic_word_embeddings/blob/main/eval/alpha-word-analogy.txt)
## Embeddings

All these word embeddings are trained on the [Clean Dataset](https://drive.google.com/file/d/1JTixpw4EvCL9M1FkPA5F4x_Cfhdp67oU/view?usp=sharing). For word2vec, the window is set to 5, which is the default. For the fasttext embeddings however, it is set to 1 as the performance drops as the window size grows. 

|            |    Word2vec   |   Fasttext    |  Alphabetized Fasttext |
| ---------- | ------------- | ------------- | ------------  |
| dims       | 300  | 300  | 300  |
|No. of Words| Content Cell  | Content Cell  | Content Cell  |
|Links       | Content Cell  | Content Cell  | Content Cell  |

If you want the fasttext model to generate word embedding for new words, [download this]() for the plain fasttext and [download this]() for the alphabetized fasttext model. 

## Citation

``` markdown
@inproceedings{mersha2020morphology,
  title={Morphology-rich Alphasyllabary Embeddings},
  author={Mersha, Amanuel and Wu, Stephen},
  booktitle={Proceedings of the 12th Language Resources and Evaluation Conference},
  pages={2590--2595},
  year={2020}
}
```

## Contact
You can contact me for more information. Would be happy to help :) Email me at amanyamy@gmail.com. Follow me on [Twitter](https://twitter.com/AmanBitz), connect with me on [LinkedIn](https://www.linkedin.com/in/leobitz/)

