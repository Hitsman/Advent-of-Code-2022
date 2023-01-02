#!/usr/bin/env python
# coding: utf-8

# In[54]:


monkeys=[]
inspections=[]
items=[]
operations=[]
divlist=[]
truelist=[]
falselist=[]

def toint(n):
    print(n)
    return(int(n))



with open('Day11Input.txt','r') as file:
    for line in file:
        line=line.rstrip()
        if "Monkey" in line:
            monkeys.append(line[7])
            inspections.append(0)
        if "Starting items" in line:
            items.append(list(map(lambda x: int(x),(line.split(':')[1].split(',')))))
        if "Operation" in line:
            oplist=[1,1,0]
            operationline=(line.split('old ',1)[1].split(' '))
            if operationline[0]=='*' and operationline[1]=='old': oplist[0]+=1
            if operationline[0]=='*' and operationline[1]!='old': oplist[1]=int(operationline[1])

            if operationline[0]=='+' and operationline[1]=='old': oplist[1]+=1
            if operationline[0]=='+' and operationline[1]!='old': oplist[2]=int(operationline[1])
            operations.append(oplist)
        if "Test" in line:
            divlist.append(int(line.split(' ').pop()))
        if 'true' in line:
            truelist.append(int(line.split(' ').pop()))
        if 'false' in line:
            falselist.append(int(line.split(' ').pop()))

            
#print(items)
#print(operations)
#print(divlist)
#print(truelist)
#print(falselist)

#print(items)


for round in range(20):
    #print('ROUND ' + str(round+1))
    for monkey in range(len(monkeys)):
        for item in items[monkey]:
            inspections[monkey]+=1
            worry=((item ** (operations[monkey][0]) * (operations[monkey][1]) + (operations[monkey][2])) //3)
            if worry% divlist[monkey]==0: items[truelist[monkey]].append(worry);throw=truelist[monkey]
            if worry% divlist[monkey]!=0: items[falselist[monkey]].append(worry);throw=falselist[monkey]
            #print(monkey, item, worry, throw)
        items[monkey]=[]
    #print(items)
print(inspections)
inspections.sort(reverse=True)
answer=inspections[0]*inspections[1]
print(answer)
if answer<=544: print('too low')


# In[ ]:




