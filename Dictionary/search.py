mydict = {"name":"Venkat",
          "age":26,
          "address":"Vijayawada"}

def search(dict,value):
    for key in dict:
        if dict[key] == value:
            return (key,value)
    return "The value does not exist"

print(search(mydict,26))