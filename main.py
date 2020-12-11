#Day 3

dataFile3 = open("day3data.txt")
d3 = dataFile3.readlines()
dataFile3.close()

def treeFinder (right, down):
  ans = 0
  pos = 0

  for i in range(0, len(d3), down):
    if (d3[i])[pos] == "#":
      ans = ans + 1 
    pos = (pos + right) % (len(d3[i]) - 1)
  
  return ans

print ("Day 3 Part 1: ", str(treeFinder(3, 1)))

#Part 2
ans2 = treeFinder(1,1) * treeFinder(3,1) * treeFinder(5,1) * treeFinder(7,1) * treeFinder(1, 2)

print ("Day 3 Part 2: ", str(ans2))

