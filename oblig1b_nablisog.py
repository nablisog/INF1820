#A
with open('dat.txt','r') as infile:
    with open('new.txt','w') as outfile:
        for words in infile:
            if words[0]=='*':
                outfile.write(words + '\n')
            else:
                line=words.split()
                if line:
                    outfile.write(line[0] + '\n')
                else:
                    pass
#B
#when comparing new.txt & dev_gold.txt,these are most repeated differences  ,>>.

#C
#(\S+|\S*[^\w\s]\S*.)

import re
infile= open('new.txt').read()
for line in infile.split():
     y= re.findall(r'\S+|\S*[^\w\s]\S*', line)
     print (y)


    
    




