# ASSIGNMENT 1 BY SHUBHAM GUPTA
# EXPERIMENT WITH 5 LIST BUILT IN FUNCTION

# Create and Print the list
mylist = ["Hi My name is shubham", "I am learning python essentials", "In Letsupgrade"]
print(mylist)

# print the Length of the list
print("The length of the list :")
print (len(mylist))

# Append list

mylist.append("And i am feeling good")
print(mylist)

# Print all Item in the list one by one
thislist = ["Hi My name is shubham", "I am learning python essentials", "In Letsupgrade"]
for i in range(len(thislist)):
  print(thislist[i])

# Insert in list
# vowel list
newlist = ['a', 'e', 'i', 'u']
newlist.insert(3, 'o')
print('Updated List:', newlist)

# EXPERIMENT WITH 5 DICTIONARY BUILT IN FUNCTION

# Create and print dictionary
thisdict =	{
  "brand": "Samsung",
  "model": "S series",
  "year": 2021,
  "Price": 40000
}
print(thisdict)

# Printing specified dictionary items
print(thisdict["brand"])
print(thisdict["model"])
print(thisdict["year"])
print(thisdict["Price"])

# Printing dictionary one by one

for x in thisdict:
  print(x)

  # Removing specified dictionary 
thisdict.pop("Price")
print(thisdict)

# Adding new items in dictionary

thisdict["color"] = "Black"
thisdict["price"] = "40,000"
print(thisdict)

#  Change items in dictionary

thisdict["Year"] = 2020
print(thisdict)