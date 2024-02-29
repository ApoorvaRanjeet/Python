a="Apoorva"
print(a[1])

# looping through the string
for x in "Apoorva":
    print(x)

# length of the string
print(len(a))

#check string
print("r" in a)

txt= "good morning mumbai"
print("india" in txt)

# check if not 
print("India" not in txt)

# Slicing 
print(a[0:])

# Modify strings 
# a="  hello, World  "
print(a.upper())
print(a.lower())
print(a.strip()) # remove whitespace
print(a.replace("hello","mellow")) # replace string
print(a.split(","))  # split the string

# concatenate string
print(a+","+txt)

# format string   : we cant concatenate number and string by this method a= 2 b= hello print(a+b)
c= 23
d= "I am Saumya , ans I am {}"
print(d.format(c))   # the format methods takes the unlimited number of arguments 

# you can also do this 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# String methods
print(a.capitalize())
print(a.casefold())
print(a.count("o"))
print(a.encode())
print(a.endswith("a"))
print(a.find("r"))
print(a.index("A"))
print(a.isalnum())
print(a.isalpha())
print(a.isascii())
print(a.islower())
