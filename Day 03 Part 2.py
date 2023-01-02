#!/usr/bin/env python
# coding: utf-8

# In[9]:


counter=0
totalscore=0
rucksacks=[]
team=0

with open('Day3Input.txt','r') as file:
    for line in file:
        rucksacks.append(line.rstrip())
#print(len(rucksacks)/3)        
for team in range(int(len(rucksacks)/3)):
    for letter in rucksacks[team*3]:
        if letter in rucksacks[team*3+1] and letter in rucksacks[team*3+2]:
            #print(letter)
            if letter.isupper(): priority=ord(letter)-38
            if letter.islower(): priority=ord(letter)-96
            totalscore+=priority
            break
        #totalscore+=priority
                
        
        #print(Container1, Container2)
        #print(rucksack)
        #counter+=1
        #if counter==5: break #this is here to test on a limited set
print(totalscore)
#if totalscore==55725: print("That's not right")


# In[ ]:




