#!/usr/bin/env python
# coding: utf-8

# In[1]:


counter = 0
with open('Day4Input.txt','r') as file:
    for line in file:
        elf=line.rstrip().split(',')
        
        listends=elf[0].split('-')
        list1=set(range(int(listends[0]),int(listends[1])+1))
        
        listends=elf[1].split('-')
        list2=set(range(int(listends[0]),int(listends[1])+1))
        
        intersection=set(list1).intersection(list2)
        if intersection:
            counter+=1

print (counter)


# In[ ]:




