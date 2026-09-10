myList = ["G","P","b","z","X"] #compare ords for alphabetical
num = 0

#start from the right
for outer in range (len(myList)-1,0,-1):
 for inner in range(outer):
   #compare two adjacent values
   if ord(myList[inner])<ord(myList[inner+1]):                  #swap ascending descending by flipping <
     #assign one of the values to a temp variable
     temp = myList[inner]
     #overwrite one of the values
     myList[inner] = myList[inner+1]
     #replace with the temp value
     myList[inner+1] = temp
     num+=1
  
print("Bubble sort complete")
print(myList)
print(num)

