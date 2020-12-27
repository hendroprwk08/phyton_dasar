thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
print(thisdict["model"])
print(len(thisdict))

#penambahan nilai
thisdict["color"] = 'red'

print(thisdict) #after the change

#check if key exist
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")