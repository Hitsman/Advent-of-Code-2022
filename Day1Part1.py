elfnumber=1
calories=0
biggestelf=0
mostcalories=0

with open('Day1Input.txt') as file:
    for line in file:
        if line.rstrip().isdigit() :        #is true if the line contains only numbers
            calories=calories+int(line)   #We need to force the program to look at the line as an integer instead of plain text and total up the calories
        if line.rstrip()=="":               #is true if the line is blank
            print("Elf #" + str(elfnumber) + " is carrying " + str(calories) + " calories.")
            if calories>mostcalories:
                mostcalories=calories
                biggestelf=elfnumber
            elfnumber+=1
            calories=0
        #print(line.rstrip(), elfnumber, calories)
        
    print("Elf #" + str(elfnumber) + " is carrying " + str(calories) + " calories.")   # Run this at the end so we don't miss the last elf (the last line isn't blank)
    if calories>mostcalories:
        mostcalories=calories
        biggestelf=elfnumber
    
    print("Pack Mule Elf #" + str(biggestelf) + " is carrying the most at " + str(mostcalories) + " calories.")
