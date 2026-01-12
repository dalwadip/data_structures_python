# make list of items
person1 = ["Harry", "Potter", "Potter"]
person2 = ["Hermione", "Granger"]
# look through important python list methods, and use them below
person1.extend(person2)# adds person 2 to the end of person 1
print(person1) # do not reassign to new variable, just print list that gets extended

person1.append("Brave") # adds value/item to end of list
print(person1) #do not reassign to new var, print list that gets appended

person1.count("Potter") # returns how many times the value shows up in list
print(person1.count("Potter")) #reassign to new var to print num or do what I did, *do this when you return something

person1.sort() # sorts the list in ascending order
print(person1)

person1.reverse() # reverses order of list
print(person1)

person1.insert(0, "Smart") # adds an element at the index
print(person1) #same here

person1.index("Potter") # returns the index of the value
print(person1.index("Potter")) #reassign to new var to print index or do what I did, *do this when you return something

person1.pop() # removes the last element at the index
print(person1) #same here

person1.copy() # returns a copy of the list
print(person1.copy()) #returns, so assign to new variable or put print on whole thing

person1.remove("Potter") # removes the first item with the index
print(person1) #same here

person1.clear() # clears the list
print(person1)

# make a set
fruits = {"banana", "apple", "cherry"}

# make a dictionary
student = {
    "name": "Andy",
    "age": 22,
    "is_kind": False
}

# make a tuple
sports = ("soccer", "basketball", "tennis")



