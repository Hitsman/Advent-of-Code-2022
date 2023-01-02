#!/usr/bin/env python
# coding: utf-8

# In[107]:


import time


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
            parsedpaths.append('v')
            
            valves[words[1]]=[int(words[4].split('=')[1].replace(';','')),parsedpaths,n]
            n+=1
    
    return(valves)


def main():
    valves=reader(16,'i')
    #print(valves)
    valvelist=[]
    for valve in valves:
        #print(valves[valve][0])
        if valves[valve][0]==0:valvelist.append(False)
        else: valvelist.append(True)
    firstvalveroom='AA'#list(valves.keys())[0]
    print(firstvalveroom)
    options=valves[firstvalveroom][1]
    #options.append('v')
    attempts=[[firstvalveroom,0,0,valvelist,options,[]]]
    # [CurrentRoom,Rate,Score,Valves,Options]
    timeleft=30
    #print(valvelist)
    minute=0
    while timeleft>0:
        minute+=1
        newattempts=[]
        print(timeleft, len(attempts))
        for attempt in attempts:
            #print(timeleft,attempt)
            for option in attempt[4]:
                if option.isupper():
                    rate=attempt[1]
                    releif=attempt[2] + attempt[1]
                    newoptions=valves[option][1]
                    #history=attempt[5]+[str(option)]
                    newattempt=([option,rate,releif,attempt[3],newoptions])#,history])
                    
                    
                valveindex=valves[attempt[0]][2]   #gets the valve position in the open/close table
                if option =='v' and attempt[3][valveindex]==True:
                    newvalves=attempt[3][:]
                    #print(valveindex,newvalves)
                    newvalves[valveindex]=False #sets valve to closed
                    releif=attempt[2] + attempt[1]
                    #print('flowrate' ,attempt[1],valves[attempt[0]][0],attempt[0])
                    flowrate=attempt[1]+valves[attempt[0]][0]
                    #history=attempt[5]+[str(option)]
                    newattempt=([attempt[0],flowrate,releif,newvalves,attempt[4]])#,history])
                
                if newattempt not in newattempts:  newattempts.append(newattempt)
        
        newattempts.sort(key=lambda x: x[2],reverse=True)
#        print(minute,newattempts[0][0:3])
        if len(newattempts)>200:
            
            attempts=newattempts[0:800]
        else:attempts=newattempts
        
        timeleft-=1
    for attempt in attempts[0:2]:
        print(attempt[0:6])
    
    #1979 is too high
    #1662 is too low
main()


# In[ ]:





# In[ ]:




