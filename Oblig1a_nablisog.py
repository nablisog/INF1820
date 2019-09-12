# encoding: utf-8
import re


"""
Question 1
1. phonetics ->speech sounds 
2. phonology->phonemes 
3. morphology->words 
4. syntax->phrases and sentences 
5. Semantics->literal meaning of phrases and sentences .
6. pragmatics->meaning in context of discourse
 
Question 2
2. Words that can stand alone to function as a words are free
morphemes while words that can’t stand alone and can only be attached to another part of words are called bound morphemes. bound morphemes are divided in to 2:-
1. prefix :- words that come before the base Eg. pre, un etc
2. suffix :- words that come after the base Eg. ish, ing etc
Example of free morphemes :- boy, man etc 

"""

with open("InO1.txt",encoding = "utf-8") as infile:
     infile = infile.read()
     counter = infile.count("er")
     c = 0
     for i in infile.split():
          if i.endswith("er"):
               c=c+1


mylist=[]             
for j in infile.split():
     mylist.append(j[-2:])



     
with open("InO1.txt","r") as file:
     with open("written.txt", "w") as file_writer:
          lines = 0
          words=0
          for l in file:
               lines = lines+1
               for w in l.split():
                    words = words+1
                    file_writer.write(w+'\n')
               
               
file.close()
file_writer.close()


print(' '.join(mylist))          
print("#"*50)          
print ("The word er is repeted",counter, "times")
print("Total amount of words ends with er are",c)
print("Total number of lines are",lines)
print("Total number of words are",words)
         

     
     
