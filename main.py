#Day 4

dataFile4 = open("day4data.txt")
d4 = dataFile4.readlines()
dataFile4.close()

ans1 = 0

passports = []
curr = ""
for i in d4:
  if i == d4[-1]:
    curr = curr + " " + i
  if i == '\n' or i == d4[-1]:
    passports.append(curr)
    curr = ""
  else:
    curr = curr + " " + i

#print (passports)

for i in passports:
  fields = i.split(' ')
  fields.pop(0)
  numFields = len(fields)
  for j in fields:
    if (j.split(":")[0] == 'cid'):
      numFields = numFields -1

  if (numFields == 7):
    ans1 = ans1 + 1   

print ("Day 4 Part 1: ", ans1)







