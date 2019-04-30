import nltk
from nltk import*
#1.1
grammar = nltk.CFG.fromstring("""
    S    ->  NP VP PP | NP VP
    VP   ->  V | V NP | V NP NP 
    PP   ->  P NP
    V    ->  "sover" | "spiser" | "gir" | "finner"
    NP   ->  "Per" | "Kari" | "Ola" | "boka" | "middag" | D N
    D    ->  "en"
    N    ->  "bok" 
    P    ->  "til"
""")
parser =  nltk.RecursiveDescentParser(grammar)
def printer(sentance):
    for i in sentance:
        for j in parser.parse(i):
            print(j)

sentance  = [["Per", "gir", "en", "bok", "til", "Kari"],
             ["Kari", "gir", "Per" ,"boka"],
             ["Ola", "sover"],
             ["Kari", "spiser"],
             ["Kari", "spiser",  "middag"],
             ["Per", "finner", "boka"]]

printer(sentance)

#1.2
s = [["Kari", "sover", "boka"], ["Ola", "finner"]]
printer(s)

#1.3
grammar2 = nltk.CFG.fromstring("""
    S    ->  NP VP PP | NP VP
    VP   ->  V | V NP | V NP NP | TV NP | TV NP NP | iTV
    PP   ->  P NP
    V    ->  "spiser"
    TV   ->  "gir" | "finner"
    iTV  ->  "sover"
    NP   ->  "Per" | "Kari" | "Ola" | "boka" | "middag" | D N
    D    ->  "en"
    N    ->  "bok" 
    P    ->  "til"
""")
parser =  nltk.RecursiveDescentParser(grammar2)
printer(sentance)
printer(s)

"""
2.1
1) number 6. leave, allow for, allow, provide
2) number 7. leave, result, lead
3) number 8. leave, depart, pull up stakes
4) number 5. exit, go out, get out, leave
5) number 3. leave (act or be so as to become in a specified state

2.2 number 5 because it's difficult to find the one that suits with the sentance

2.3 number 3 & 7 because both of them refer on a point to something that is
resulted due to the presence of something.


"""
"""
since the questions weren't asked to be answered using specific method, i used
my own way to answer 3.1 &3.2
"""
#3.1
infile = open ("wsd_tren.txt").read()
count=infile.count("Removing")
y= (count/16.)*100.
# the Probability of removing is 12.5%
print ( "the probability of Removing is", y,"%" )

#3.2
#when doing this question, in the txt file, i only put sentences which start
#with Reading so my counter doesn't count day from the non needed part
#P(day|Reading)---> p(3/8)---> 0.375x100---->37.5%
infile = open ("wsd_tren.txt").read()
counte=infile.count("day")
counter=infile.count("Reading")
x=(counte/counter)*100
# The Probability of P(day|Reading) is 37.5%
print ("The Probability of P(day|Reading) is", x,"%")













