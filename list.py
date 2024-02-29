l=["apoorva","aadrika","anusha","anusha"]
print(l)

print(len(l))


l2=[1,"c","3.98","akku",True]
print(l2)
print(len(l2))
print(type(l2))

# we acn use list() constructor to create list
l3 =(("1",True,False))
print(l3)

#Access the list items
print(l3[0])
print(l3[-1])

print(l2[-4:-1])

# check if item exist 
if "apoorva" in l:
    print("yes")

# change item value

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist[1:2]=["hello","how","when"]
print(thislist)

thislist.insert(3,"watermelon")
print(thislist)

# adding item to the list
# append 
thislist.append("juice")
print(thislist)

# extend
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# remove 
# thislist.remove("kiwi")
# print(thislist)

# # del
# del thislist[0]
# print(thislist)

# del thislist

# #clear
# thislist.clear()
# print(thislist)

# loop through a list

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#loop through index
for i in range(len(thislist)):
  print(thislist[i])



i=0
# using while loop
while i < len(thislist):
    print(thislist[i])
    i+=1

# looping using list comprehension

[print(i) for i in thislist]

newlist=[]
for x in thislist:
    if "a" in x:
        newlist.append(x)

newlist=[x for i in thislist if "a" in x]

newlist = [x for x in newlist if x !="apple"]
    
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
thislist.sort(reverse=True)
print(thislist)

#join
mylist = thislist.copy()
print(mylist)
list3 = thislist+mylist
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)