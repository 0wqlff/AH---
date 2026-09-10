myList = ["G","X","b","P","z"] #since alphatbetical notice comparing ord, for numerical would just compare numbers
num=0

for index in range (1,len(myList)):
    currentvalue = myList[index]
    position = index


    while position > 0 and ord(myList[position-1])>ord(currentvalue):     #swap ascending and descending by flipping the second >    
        myList[position] = myList[position-1]
        position -= 1
        num+=1

    myList[position] = currentvalue

print(myList)
print(num)
