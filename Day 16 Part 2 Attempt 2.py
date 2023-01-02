#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
start=time.time()


def reader(day,inputorsample):
    if inputorsample=='i': word='Input'
    if inputorsample=='s': word='Sample'
    sensorlist=[]
    beaconlist=[]
    
    filename='Day'+str(day)+str(word)+'.txt'
    valves={}
    n=0
    with open(filename,'r') as file:
        for line in file:
            line=line.rstrip()
            words=line.split(' ')
            paths=line.split('valve')[1].split(' ')
            parsedpaths=[]
            for tunnel in paths:
                if ',' in tunnel: tunnel=tunnel.replace(',','')
                if tunnel.isupper():parsedpaths.append(tunnel)
            #parsedpaths.append('v')
            
            valves[words[1]]=[int(words[4].split('=')[1].replace(';','')),parsedpaths,n]
            n+=1
    
    return(valves)

def mapgen(valves):
    map={}
    for room1 in valves:
        if valves[room1][0]==0 and room1!='AA': continue
        
        for room2 in valves:
            if valves[room2][0]==0: continue
            if room1==room2: continue
            currentroom=[room1]
            step=0
            paths=[[room1]]
            foundpath=False
            while foundpath==False:
                step+=1
                newpaths=[]
                newcurrentroom=[]
                if step>20: print('error');break
                
                for n in range(len(paths)):
                    options=valves[currentroom[n]][1]
                    #print(currentroom,options)###########################
                    if room2 in options: foundpath=True;break
                    for option in options:
                        if option in paths[n]:continue
                        if option in newcurrentroom:continue
                        optionlist=[option]
                        newpaths.append(paths[n]+optionlist)
                        newcurrentroom.append(option)
                paths=newpaths
                #print('Paths ',paths,room1,room2)
                currentroom=newcurrentroom
                
                    
            map[room1+room2]=step
    #print('Map ',map)
    return(map)
                
def recursion(valvemap,path,remainingoptions,timeleft,completedpaths):
    print('recursionstart',remainingoptions, path)
    remainingoptions.remove(path[-1])
    print('remaining',remainingoptions)
    if timeleft<0 or len(remainingoptions)==0:
        completedpaths=[path,remainingoptions]
        return(completedpaths)
    for r in remainingoptions:
        print('option',r)
        optiontime=timeleft-(valvemap[path[-1]+r]+1)
        newpath=path+[r]
        print('newpath',newpath,timeleft)
        recursed=recursion(valvemap,newpath,remainingoptions,optiontime,completedpaths)
        print('recursed',recursed)
        completedpaths.append(recursed)
        
    return(completedpaths)
        
def pathselection(valvemap,valves,score,hpath,epath,remainingoptions,htimeleft,etimeleft):
    paths=[]
    for option1 in remainingoptions:
        
        hoptiontime=htimeleft-(valvemap[hpath[-1]+option1]+1)
        optionsleft=remainingoptions[:]
        if hoptiontime>=0:
            newhpath=hpath+[option1]
            newhscore=valves[option1][0]*hoptiontime
            optionsleft.remove(option1)
        else:
            newhpath=hpath
            newhscore=0
            
        for option2 in optionsleft:
            if option1==option2:continue

            eoptiontime=etimeleft-(valvemap[epath[-1]+option2]+1)
            secondoptionsleft=optionsleft[:]
            if eoptiontime>=0:
                newepath=epath+[option2]
                newescore=valves[option2][0]*eoptiontime
                secondoptionsleft.remove(option2)
            else:
                newepath=epath
                newescore=0
                    
            thisscore=score+(newhscore+newescore)
            paths.append([thisscore,newhpath,newepath,secondoptionsleft,hoptiontime,eoptiontime])
    return(paths)
            
def printeach(thing):
    for each in thing:
        print(each)
    return()

# [CurrentRoomHuman, CurrentRoomElephant,Rate,Score,Valves,OptionsHuman, OptionsElephant]

def main():
    valves=reader(16,'i')
    #print(valves)
    valvemap=mapgen(valves)
#    for path in valvemap:
#        print(path,valvemap[path])
    minutes=26
    path=['AA']
    remainingoptions=['AA']
    for valve in valves:
#        print(valves[valve])
        if valves[valve][0]!=0:
            remainingoptions.append(valve)
#    print(remainingoptions)
    timeleft=26
    completedpaths=[]
#    completedpaths=recursion(valvemap,path,remainingoptions,timeleft,completedpaths)
#    print('map' , mapgen(valves))
#    print(len(completedpaths))
    for path in completedpaths:
        print(path)
        
    #printeach(valvemap
#           score,newhpath,newepath,optionsleft,hoptiontime,eoptiontime
    remainingoptions.remove("AA")
    
    paths=[[0,["AA"],["AA"],remainingoptions,timeleft,timeleft]]
    newpaths=[]
    donepaths=[]
    n=0
    while paths:
        n+=1
        if n==20:break
        newpaths=[]
        print(len(paths))

        for path in paths:
            #print(path)
            if path[4]>0 and path[5]>0:
                newpathset=pathselection(valvemap,valves,path[0],path[1],path[2],path[3],path[4],path[5])
                if newpathset: newpaths+=newpathset
                else:donepaths.append(path)
            else: donepaths.append(path)
        if len(newpaths)<20000:
            newpaths.sort(key=lambda x: (x[0]), reverse=True)
            for n in range(len(newpaths)-1):
                if newpaths[n][0]==newpaths[n+1][0]:
                    newpaths[n+1][0]=0
        if len(newpaths)>20000:
            newpaths.sort(key=lambda x: (x[0]), reverse=True)
            #for x in range(10):
            #    print(newpaths[x])
        paths=newpaths[0:150000]
        
    donepaths.sort(key=lambda x: (x[0]), reverse=True)
    for x in range(5):
        print(donepaths[x])
    for x in range(100):
        print(donepaths[x][0])
    print(len(donepaths))
    #print(newpaths)
        
    #2821 is too high
    #2456 is too low
    #2473 is the right answer
main()
print(round(time.time()-start,4))

