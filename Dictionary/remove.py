mydict = {"name":"Venkat",
          "age":26,
          "address":"Vijayawada"}

# del mydict['age']
# print(mydict)

# remove = mydict.pop("age")
# print(remove)

remove = mydict.pop("ag",None) # if key is not present in dictionary pop returns error so to avoid we can give default value that is None
print(remove)

mydict.popitem() # Delets last key value pair

mydict.clear() # delets all elements from the dictionary