thistuple = ("akku","sonu","chinu","karti")

print(thistuple[1])
print(thistuple[-1])
print(thistuple[0:3])

# chekc if item exist in tuple 
if "akku" in thistuple:
    print("yes")
else:
    print("no")

y= list(thistuple)
print(y)
y.append("aditi")
thistuple = tuple(y)
print(thistuple)
# del thistuple
# print(thistuple)

# loop through tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

i=0
for i in range(len(thistuple)):
    print(thistuple[i])

i=0   
while i<len(thistuple):
    print(thistuple[i])
    i+=1