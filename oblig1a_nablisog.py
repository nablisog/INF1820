# encoding: utf-8
#A
infile= open("dat.txt")
print (infile.read())
infile.close()
#B
counter=0
infile = open ("dat.txt").read()
count=infile.count("er") #how many times the character is present in the text.    
for word in infile.split():
     if word.endswith("er"):
          counter=counter+1 # counts every word that ends with er 
     else:
          pass
		
		
print ('Words that endswith er are  %d .' % counter)
print ('The character er is present in the text %d times.' % count)

#C
My_list=[]
infile = file("dat.txt").read()
for word in infile.split():
 # putting the last 2 letters of every word into Mylist
     My_list.append(word[-2:]) 
     streng=" ".join(My_list)
     

#D
lines=0; words=0
infile= open("dat.txt","r")
for line in infile:
     word=line.split(" ") # deler opp hver linje basert på mellomrom
     lines=lines+1 # counting lines in the file
     words=words+len (word) # counting words in the file


 
print ('The total words in the file are  %d .' % words)
print ('The total lines in the file are  %d .' % lines)
infile.close()
          
          
          


          
          
