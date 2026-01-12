# make list of items, ordered, changeable
print("Lists and their functions/methods")
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
print()

# make a set, unordered, changeable
print("Sets and their functions/methods")
fruits = {"banana", "apple", "cherry"}
veggies = {"carrot", "pepper", "corn"}
# look through set methods
fruits.add("orange") # adds element to set
print(fruits)

copy = fruits.copy() # returns copy of set
print(copy)

# diff = fruits.difference(veggies) # returns set containing differences between 2 or more sets
# print(diff)
#
# fruits.difference_update(veggies) # removes the items in this set that are also included in another
# print(fruits)

fruits.discard("apple") # removes specified item
print(fruits)

# inter = fruits.intersection(veggies) # returns set, that is intersection of 2 other sets
# print(inter)
#
# fruits.intersection_update(veggies) # removes the items in this set that are not present in other
# print(fruits)
#
# disjoint = fruits.isdisjoint({"apple"}) # returns if two sets have an intersection or not (param must be a set)
# print(disjoint)
#
# sub = fruits.issubset({"banana"}) # returns True if all items of this set is present in another set (param must be a set)
# print(sub)
#
# sup = fruits.issuperset({"orange"}) # returns True if all items of another set is present in this set (param must be a set)
# print(sup)

fruits.remove("cherry") # removes specified element
print(fruits)

fruits.pop() # removes a RANDOM element from the set, random b/c it's a set
#**NOTE: set is unordered, so pops random element, which could be same item as remove, could put remove before pop
print(fruits)

# union = fruits.union(veggies) # return a set containing the union of sets
# print(union)
#
# fruits.update(veggies) # update the set with the union of this set and others
# print(fruits)

fruits.clear() # clears set
print(fruits)
print()

# make a dictionary
student = {
    "name": "Andy",
    "age": 22,
    "is_kind": False
}

# make a tuple
sports = ("soccer", "basketball", "tennis")



