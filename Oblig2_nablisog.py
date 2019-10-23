#encoding=utf-8
import nltk
from nltk import word_tokenize
import re
from collections import Counter
from nltk.corpus import gutenberg



"""
1.
A statistical language model uses corpus frequencies
to calculate the probability of word sequences

P(synger|kari) = C(kari,synger)/C(kari)

P(kari|<s>)∗P(synger|kari)∗P(ikke|synger)∗P(<\s>|ikke)
1/3*1/1*2/3*2/2

"""
probablity = (1/3)*(1/1)*(2/3)*(2/2)
print("probablity:-", probablity)



"""
2.
Jeg = pronomen
spiser = verb
sushi = substantiv
med = preposisjon
pinner = substantiv

"""



bible_word= []
file_reader = gutenberg.words("bible-kjv.txt")
counter = Counter(file_reader)

for i in file_reader:
    bible_word.append(i.lower())

reader = gutenberg.sents("bible-kjv.txt")
four = reader[3]
five = reader[4]


print("Total token are:", len(file_reader))
print("Total type of words are:", len(set(bible_word)))
print("The Most 20 common words are:",counter.most_common(20))
print("The word heaven appears: ",counter["heaven"])
print("The word death appears: ",counter["death"])
print("The word life appears",counter["life"])
print("The fouth sentence:", reader[3])
print("The fifth sentence", reader[4])



print("#"* 25)

patterns = [(r'.*ing$', 'VBG'),
            (r'.*ed$', 'VBD'),
            (r'.*es$', 'VBZ'),
            (r'.*ould$', 'MD'),
            (r'.*\'s$', 'NN$'),
            (r'.*s$', 'NNS'),
            (r'ˆ-?[0-9]+(.[0-9]+)?$', 'CD'),
            (r'.*', 'NN')]


regexp_tagger = nltk.RegexpTagger(patterns)
tagg = []
with open ("sentence.txt", 'r') as infile:
    with open ("tagg.txt", 'w') as outfile:
        for j in infile:
            tagg = word_tokenize(j)
            tagg.append(regexp_tagger.tag(tagg))

            for k in tagg:
                outfile.write(str(k)+'\n')
