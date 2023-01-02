#!/usr/bin/env python
# coding: utf-8

# In[75]:


def path(currentpath):
    string='root/'
    for dir in currentpath:
        string=string+dir+'/'
    return(string)

sizelist=[]
currentpath=[]
linenumber=0
with open('Day7Input.txt','r') as file:
    for line in file:
        linenumber+=1
        #if linenumber>50:break
        if '$' in line:
            command=line.rstrip().split(' ')
            if command[1]=='cd':
                if command[2]=='/' :currentpath=[]
                elif command[2]=='..':currentpath.pop()
                else: currentpath.append(command[2])
        else:
            resp=line.rstrip().split(' ')
            if resp[0].isnumeric(): 
                sizelist.append(path(currentpath)+resp[0])
                #print('currentpath ' + str(currentpath))
sizelist.sort()
sizeary=[]
for file in sizelist:
    sizeary.append(file.split('/'))

stillfolders=1
folderlist=[]
foldersizes=[]
level=0

for file in sizelist:
    #print(file)
    file,size=file.rsplit('/',1)
    while '/'in file:
        
        if file in folderlist:
            foldersizes[folderlist.index(file)]+=int(size)
        else: folderlist.append(file);foldersizes.append(int(size))
        file,subfolder=file.rsplit('/',1)
        
        #for l in range(len(folderlist)): print(folderlist[l],foldersizes[l])
        #print()
        
sumsize=0
for size in foldersizes:
    if size<=100000:sumsize+=size
print (sumsize)
if sumsize<=1104798 or sumsize>=1916471: print("Something's wrong")

#for n in range(len(folderlist)):
#    print(folderlist[n],foldersizes[n])

