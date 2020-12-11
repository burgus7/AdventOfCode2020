#print("Welcome to the super expense report fixer upper program .jpg 2000 inator!")

dataFile = open("data.txt")
data = dataFile.readlines()
dataFile.close()

for i in range (len(data)):
  data[i] = int(data[i])

for i in range (len(data)):
  complementaryNum = 2020 - data[i]
  for j in range (len(data)):
    if data[j] == complementaryNum:
      x = data[i]
      y = data[j]

print ("part 1: " + str(x*y))

# stop killing it gosh, save it and make a new solution in somewhere else