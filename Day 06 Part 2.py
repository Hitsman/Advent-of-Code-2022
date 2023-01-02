#!/usr/bin/env python
# coding: utf-8

# In[10]:


with open('Day6Input.txt','r') as file:
    for line in file:
        received=line.rstrip()
#print(received)

for position in range(len(received)):
    if received[position+0] not in received[position+1:position+4] and \
       received[position+1] not in received[position+2:position+4] and \
       received[position+2] not in received[position+3:position+4]:
        print(position+4, received[position+0:position+4])
        break
    


# In[ ]:




