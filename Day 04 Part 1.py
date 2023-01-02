#!/usr/bin/env python
# coding: utf-8

# In[35]:


counter = 0
with open('Day4Input.txt','r') as file:
    for line in file:
        elf=line.rstrip().split(',')
        
        listends=elf[0].split('-')
        list1=set(range(int(listends[0]),int(listends[1])+1))
        
        listends=elf[1].split('-')
        list2=set(range(int(listends[0]),int(listends[1])+1))
        
        #intersection=set(list1).intersection(list2)
        if list1==list2 or list1.issubset(list2) or list2.issubset(list1):
           # print ("Both", line)
            counter+=1
        #elif list1.issubset(list2): print("1",line) 
        #elif list2.issubset(list1): print("2",line)
        
        #print(line)

        #if counter==5: break
print (counter)


# In[ ]:




