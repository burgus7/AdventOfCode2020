#print("Welcome to the super expense report fixer upper program .jpg 2000 inator!")

dataFile = open("data.txt")
data = dataFile.readlines()
dataFile.close()

for i in range (len(data)):
  data[i] = int(data[i])

for i in range (len(data)):
  for j in range (len(data)):
    sum = data[i] + data[j]
    if sum == 2020:
      num1 = data[i]
      num2 = data[j]

print ("part 1: " + str(num1*num2))

# stop killing it gosh, save it and make a new solution in somewhere else okay done :)

for i in range (len(data)):
  for j in range (len(data)):
    for k in range (len(data)):
      sum = data[i] + data[j] + data[k]
      if sum == 2020:
        num1 = data[i]
        num2 = data[j]
        num3 = data[k]

print ("part 2: " + str(num1*num2*num3))