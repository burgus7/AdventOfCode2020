#Day 3

dataFile3 = open("day3data.txt")
d3 = dataFile3.readlines()
dataFile3.close()

ans1 = 0

pos = 0
for i in d3:
  if i[pos] == "#":
    ans1 = ans1 + 1 #that means we hit a tree
  pos = (pos + 3) % (len(i) - 1)

print ("Day 3 Part 1: ", str(ans1))