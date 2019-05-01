import nltk
from nltk.corpus import* 
from nltk.corpus import brown
bwords = nltk.FreqDist( w.lower() for w in brown.words ())
btags = nltk.FreqDist(tag for (word, tag) in brown.tagged_words())
print (btags.tabulate (10))
print (bwords.tabulate (10))


cfd = nltk.ConditionalFreqDist(brown.tagged_words())
tags = brown.tagged_words()
pos_tags = [val for key, val in tags]
conditions = cfd.conditions()
fd = nltk.FreqDist(pos_tags)
b=0
for c in conditions:
	if cfd[c]['NN']:
             b=b+1

print ("In brown corpus there are %d nouns" % b)

# finding most frequent nouns
# it takes lots of time to execute this code
import nltk
from nltk.corpus import brown
brown =nltk.corpus.brown.tagged_words(categories="news")
nouns = []
for word, tag in brown:
   if tag[:2] == "NN":
      nouns.append(word + "/" + tag)
      x = nltk.FreqDist(nouns)

print (x.most_common(5))

import nltk
from nltk.corpus import brown
c=0
for word, pos in brown.tagged_words():
     if word== "linguist":
          c=c+1

print ("the word linguist is occured %d times" % c)

#finding most frequent adjective

brown =nltk.corpus.brown.tagged_words(categories="news")
adjectives = []
for w, t in brown:
   if t[:2] == "ADJ":
      adjectives.append(w + "/" + t)
      nfd= nltk.FreqDist(adjectives)
      print (nfd.most_common(5))
      

brown = nltk.corpus.brown.tagged_words()
brown = sorted([(word.lower(), tags) for word, tags in brown])
tags = [tag for (word,tag) in brown]
td = nltk.FreqDist(tags)
dd= nltk.FreqDist(word)
print (td)
#most frequent tag
print (td.max())
print (dd)
#tags that often follows nouns
from collections import defaultdict
from nltk.corpus import brown
import nltk
after = defaultdict(int)
for line in nltk.bigrams(brown.tagged_words()):
    if line[0][1].startswith("NN"):
        nextTag = line[1][1]
        after[nextTag] += 1

for tag in sorted(after, key=lambda i: int(after[i]), reverse=True):
    print(tag, after[tag])


#2 when comparing the probability of a & b through using codes from question one,
# b's reading is more likely than a 
    


from nltk.chunk import RegexpParser
chunker = RegexpParser(r'''
                    NP:
                    {<DT><.*>*<NN.*>}
                    <NN.*>}{<.*>
                    <.*>}{<DT>
                    <NN.*>{}<NN.*>
                    ''')

sent = [('the', 'DT'), ('sushi', 'NN'), ('roll', 'NN'), ('was',
'VBD'), ('filled', 'VBN'), ('with', 'IN'), ('the', 'DT'), ('fish',
'NN')]
chunker.parse(sent)
print (chunker)

import nltk
from nltk.chunk import RegexpParser
grammar = '''
NP: {<DT>?<JJ>*<NN>*}
V: {<V.*>}'''
chunker = nltk.RegexpParser(grammar)
s=  [('the', 'DT'), ('sushi', 'NN'), ('roll', 'NN'), ('was',
'VBD'), ('filled', 'VBN'), ('with', 'IN'), ('the', 'DT'), ('fish',
'NN')]
chunked = chunker.parse(s)
chunked.draw()
print (chunked)

'''
# for extracting noungroups and verbgroups
for line in chunked:
    if isinstance(line, nltk.tree.Tree):               
        if line.node == "NP":
            do_something_with_subtree(line)
        else:
            do_something_with_leaf(line)
'''
'''
chunk.RegexpParser with 1 stages:
RegexpChunkParser with 4 rules:
       <ChunkRule: '<DT><.*>*<NN.*>'>
       <SplitRule: '<NN.*>', '<.*>'>
       <SplitRule: '<.*>', '<DT>'>
       <MergeRule: '<NN.*>', '<NN.*>'>
(S
  (NP the/DT sushi/NN roll/NN)
  (V was/VBD)
  (V filled/VBN)
  with/IN
  (NP the/DT fish/NN))
  '''

from nltk.corpus import conll2000
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
training_chunks = conll2000.chunked_sents("train.txt", chunk_types=["NP"])
test_chunks = conll2000.chunked_sents("test.txt", chunk_types=["NP"])
print (cp.evaluate(training_chunks))
print (cp.evaluate(test_chunks))

'''
ChunkParse score:
    IOB Accuracy:  61.0%%
    Precision:     46.5%%
    Recall:        25.4%%
    F-Measure:     32.9%%
ChunkParse score:
    IOB Accuracy:  59.7%%
    Precision:     45.3%%
    Recall:        24.2%%
    F-Measure:     31.6%%

'''

grammar = 'NP: {<[CDJNP].*>+}'
cp = nltk.RegexpParser( grammar )
print (cp.evaluate(test_chunks))
print (cp.evaluate(training_chunks))

'''
ChunkParse score:
    IOB Accuracy:  87.7%%
    Precision:     70.6%%
    Recall:        67.8%%
    F-Measure:     69.2%%
ChunkParse score:
    IOB Accuracy:  87.4%%
    Precision:     69.7%%
    Recall:        67.5%%
    F-Measure:     68.6%%

'''
