#!/usr/bin/env python
# coding: utf-8

# In[38]:


counter=0
totalscore=0

with open('Day3Input.txt','r') as file:
    for line in file:
        rucksack=line.rstrip()
        size=int(len(rucksack)/2)
        
        Container1=rucksack[0:size]
        Container2=rucksack[size:size*2]
        
   
        for letter in Container1:
            if letter in Container2:
                if letter.isupper(): priority=ord(letter)-38
                if letter.islower(): priority=ord(letter)-96
                #print(letter, priority, Container1, Container2)
                break
        totalscore+=priority
                
        
        #print(Container1, Container2)
        #print(rucksack)
        #counter+=1
        #if counter==5: break #this is here to test on a limited set
print(totalscore)
if totalscore==55725: print("That's not right")


# In[ ]:




