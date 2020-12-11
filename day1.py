#Day 1 Part 1

dataFile = open("data.txt")
data = dataFile.readlines()
dataFile.close()

for i in range (len(data)):
  data[i] = int(data[i])

data.sort()

for i in range (len(data)):
  for j in range (len(data)):
    jIndex = len(data)-j-1
    sum = data[i] + data[jIndex]
    if sum == 2020:
      num1 = data[i]
      num2 = data[jIndex]

print ("Day 1 Part 1: " + str(num1*num2))

for i in range (len(data)):
  for j in range (len(data)):
    for k in range (len(data)):
      kIndex = len(data)-k-1
      sum = data[i] + data[j] + data[kIndex]
      if sum == 2020:
        answer2 = data[i]*data[j]*data[kIndex]

print ("Day 1 Part 2: " + str(answer2))

