#!/usr/bin/env python
# coding: utf-8

# In[18]:


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
    path=file.split('/')
    size=path.pop()
    while len(path)>0:
        filepath=''
        for dir in path:
            filepath+=dir+'/'
        #filepath.rstrip('/')
        if filepath in folderlist:
            foldersizes[folderlist.index(filepath)]+=int(size)
        else: folderlist.append(filepath);foldersizes.append(int(size))
        path.pop()
        
        #for l in range(len(folderlist)): print(folderlist[l],foldersizes[l])
        #print()
        
sumsize=0
for size in foldersizes:
    if size<=100000:sumsize+=size
print (sumsize)
if sumsize==1886043: print("CORRECT!")

totalfilesystemsize=70000000
spacefree=totalfilesystemsize-foldersizes[0]
print(foldersizes[0],spacefree)
neededspace=30000000
spacetofreeup=neededspace-spacefree
print(spacetofreeup)
foldersizes.sort()
#print (foldersizes)

for size in foldersizes:
    if size>=spacetofreeup: print(size);break

#for i in range(len(folderlist)):
#    print(folderlist[i],foldersizes[i])


# In[ ]:




