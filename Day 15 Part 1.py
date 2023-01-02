#!/usr/bin/env python
# coding: utf-8

# In[50]:


def reader(day,inputorsample):
    if inputorsample=='i': word='Input'
    if inputorsample=='s': word='Sample'
    sensorlist=[]
    beaconlist=[]
    
    filename='Day'+str(day)+str(word)+'.txt'
    with open(filename,'r') as file:
        for line in file:
            line=line.rstrip()
            words=line.split(' ')
            sensor=[int(words[2].split('=')[1].replace(',',''))   ,   int(words[3].split('=')[1].replace(':',''))]
            beacon=[int(words[8].split('=')[1].replace(',',''))   ,   int(words[9].split('=')[1])]
            sensorlist.append(sensor)
            beaconlist.append(beacon)
    
    return(sensorlist,beaconlist)


def main():
    sensors,beacons=reader(15,'i')
    distances=[]
    for n in range(len(beacons)):
        distances.append(abs(beacons[n][0]-sensors[n][0])+abs(beacons[n][1]-sensors[n][1]))

        
    y=2000000
    covered=set()
    for n in range(len(sensors)):
        strength=distances[n]-abs(sensors[n][1]-y)
        if strength>0:
            coveredrow=set()
            for m in range(-strength,strength+1):
            #    singlecover.append(sensors[n][0]+m)
                #if sensors[n][0]+m not in covered:
                covered.add(sensors[n][0]+m)
            #covered=set(coveredrow)
    for beacon in beacons:
        if beacon[0] in covered and beacon[1]==y:
            #print('removed')
            covered.discard(beacon[0])
    print()        
    #print(distances)
    #print(covered)
    print(len(covered))
    #print(sensors,beacons)
    #for n in range(len(sensors)): print(n,sensors[n],distances[n])
    
    
main()


# In[ ]:




