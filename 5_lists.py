friends = ["Kevin", "Karen", "Jim", "Frank", "Frank", "Frank", "Frank", "James"]
numbers = [3, 543, 6, 34, 657, 9, 57]
friends2 = ["Kevin", "Karen", "Jim", "Frank", "Frank", "Frank", "Frank", "James"]

print(friends)
print(friends[2])
print(friends[-2])  #you can use negative numbers to choose elements
print(friends[1:])  #print all elements to the right another element
print(friends[1:4]) #print all elements in range, but not last element
friends[1] = "Mike" #replace element in array
print(friends[1])
friends.extend(numbers)    #you can combine a list of numbers and a list of strings
print(friends)
friends.append("Toby")     #add element to end of list
print(friends)
friends.insert(2, "Kelly") #insert element in specific spot in a list
print(friends)
friends.remove("Jim")      #remove element from list
print(friends)
friends.pop()              #remove last element of list - pop
print(friends)
print(friends.index("James")) #return list position of a string
print(friends.count("Frank")) #count instances of a string in a list
friends2.sort()               #sort list in alphabetical order
print(friends2)
numbers.sort()                #sort numbers in a list from lowest to highest
print(numbers)
numbers.reverse()             #reverse order of numbers in a list
print(numbers)
friends3 = friends.copy()     #copy list into new list
print(friends3)
#friends.clear()              #clear list
#print(friends)