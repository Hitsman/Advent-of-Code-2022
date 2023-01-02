#!/usr/bin/env python
# coding: utf-8

# In[17]:


d={'X':1,'Y':2,'Z':3}    #This is a dictonary of letters and their points

#Here is a matrix of who wins what games
w={
    'A X':3, 'A Y':6, 'A Z':0, 
    'B X':0, 'B Y':3, 'B Z':6, 
    'C X':6, 'C Y':0, 'C Z':3,
  }


counter=0
totalscore=0

with open('Day2Input.txt','r') as file:
    for line in file:
        points=line.rstrip().split()
        you=(d[points[1]])
        
        matchpoints=w[line.rstrip()]
        
        totalscore+=(you+matchpoints)
        #print(elf, you, totalscore)
        #counter+=1
        #if counter==50: break #this is here to test on a limited set
print(totalscore)
if totalscore ==14731: print("something's still wrong")


# In[ ]:




