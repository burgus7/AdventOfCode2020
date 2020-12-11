#Day 2

dataFile2 = open("day2data.txt")
d2 = dataFile2.readlines()
dataFile2.close()

ans1 = 0

for i in d2:
  currLine = i.split(" ")
  
  range = currLine[0].split("-")
  low = int(range[0]) 
  high = int(range[1])
  
  letter = currLine[1].split(":")[0] 

  counter = 0
  for j in currLine[2]:
    if j == letter: 
      counter = counter + 1
      
  if counter <= high and counter >= low:
    ans1 = ans1 + 1

print ("Day 2 Part 1: " + str(ans1))

ans2 = 0

for i in d2:
  currLine = i.split(" ")
  
  range = currLine[0].split("-")
  pos1 = int(range[0]) - 1 
  pos2 = int(range[1]) - 1
  
  letter = currLine[1].split(":")[0] 

  password = currLine[2]
  
  cond1 = (password[pos1] == letter)
  cond2 = (password[pos2] == letter)
  if (cond1 != cond2):
    ans2 = ans2 + 1
    
print ("Day 2 Part 2: " + str(ans2))


#def meme(ack):
#  print("A" * ack + "CK")


#meme(69)
