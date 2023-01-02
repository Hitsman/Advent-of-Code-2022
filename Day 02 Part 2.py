#!/usr/bin/env python
# coding: utf-8

# In[5]:


d={'A':1,'B':2,'C':3}    #This is a dictonary of letters and their points
m={'X':0,'Y':3,'Z':6}    #This is a dictonary of match outcomes and their points


#Here is a matrix of what you need to throw to win (Z), tie (Y), or lose (X) and your associated points
w={
    'A X':'C', 'A Y':'A', 'A Z':'B', 
    'B X':'A', 'B Y':'B', 'B Z':'C', 
    'C X':'B', 'C Y':'C', 'C Z':'A',
  }


counter=0
totalscore=0

with open('Day2Input.txt','r') as file:
    for line in file:
        yourhand=(w[line.rstrip()])
        
        yourpoints=(d[yourhand])
        
        lineread=line.rstrip().split()
        match=lineread[1]
        matchpoints=m[match]
        
        totalscore+=(yourpoints+matchpoints)
        #print(lineread, yourhand, yourpoints, matchpoints, totalscore)
        #counter+=1
        #if counter==5: break #this is here to test on a limited set
print(totalscore)


# In[ ]:




