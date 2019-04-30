# encoding: utf-8

import nltk
from nltk import bigrams
from nltk.probability import ConditionalFreqDist, FreqDist, ConditionalProbDist, LaplaceProbDist

class LM:
    def __init__(self):
        self.bigrams = ConditionalFreqDist()
        self.unigrams = FreqDist()
        sentences = nltk.corpus.brown.sents(categories=nltk.corpus.brown.categories()[1:])

        for sent in sentences:
            sent = [None] + sent + [None]
            for prev, word in bigrams(sent):
                self.bigrams[prev].inc(word)
                self.unigrams.inc(word)

        self.bigrams = ConditionalProbDist(self.bigrams, LaplaceProbDist)
        self.unigrams = LaplaceProbDist(self.unigrams)

    def p(self, w, prev):
        p = 0.5*self.unigrams.prob(w)
        if prev in self.bigrams:
            p += self.bigrams[prev].prob(w)
        return p

    def logprob(self, s):
        p=0
        for x, y in self.bigram(s):
            p = p+log (self.p (x,y), 2)
        return p

    def perplexity(self, sents):
        l=0
        N=0

        for line in sents:
            l += self.logprob(line)
            N += len(line)

            perplexity = pow(2, -l / N)

        return perplexity

    #when comparing, perplexity of adventrue is higher than news


import nltk
from collections import Counter
brown = nltk.corpus.brown.tagged_words(categories="news") 


def zipfity(lst):
    frequencies = FreqDist(lst).most_common(10)
    k = frequencies[0][1]
    r = 1

    for element in frequencies:
        print(r, element[0], "Observed frequency:", element[1], "Zipf:", k / r)
        r += 1
        

import nltk
from nltk import RegexpTagger 
brown = nltk.corpus.brown.tagged_words(categories="adventure")
brown = sorted([(word.lower(), tags) for word, tags in brown])
word_patterns = [
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
    (r'.*ould$', 'MD'),
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*ness$', 'NN'),
    (r'.*ment$', 'NN'),
    (r'.*ful$', 'JJ'),
    (r'.*ious$', 'JJ'),
    (r'.*able$', 'ADJ'),
    (r'.*ic$', 'JJ'),
    (r'.*ive$', 'JJ'),
    (r'.*ic$', 'JJ'),
    (r'.*est$', 'JJ'),
    (r'^a$', 'PREP'),
]

regexp_tagger = nltk.RegexpTagger(word_patterns)
regexp_tagger.tag(brown)
x=LM.RegexpTagger(brown)

import re
infile= open('test_setninger.txt').read()
for line in infile.split():
     y= re.findall(r'\S+|\S*[^\w\s]\S*', line)
     print (y)



        

        
