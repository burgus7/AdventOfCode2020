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

print (x, y, x+y)
print (x*y)

#idk if this is right but i have to stop now. food time. 
# aw sad, test it! submit the number and see

# you have telememe open right? yeah


#dataList = dataString.split("\n")

# You can 100% do this challenge :) <3