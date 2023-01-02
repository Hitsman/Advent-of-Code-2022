elfnumber=1
calories=0
elflist=[]

with open('Day1Input.txt') as file:
    for line in file:
        if line.rstrip().isdigit() :        #is true if the line contains only numbers
            calories=calories+int(line)   #We need to force the program to look at the line as an integer instead of plain text and total up the calories
        if line.rstrip()=="":               #is true if the line is blank
            elflist.append(calories)
            calories=0
        
        
    elflist.append(calories)   # Run this at the end so we don't miss the last elf (the last line isn't blank)

elflist.sort(reverse=True)
print(elflist[0],elflist[1],elflist[2],elflist[3])
print(elflist[0]+elflist[1]+elflist[2])
