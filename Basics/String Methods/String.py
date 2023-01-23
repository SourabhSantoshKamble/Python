# String methods demonstration

# String initialization
str1 = "HELLOWORLD"
str2 = "hello 123 hello"
str3 = "    "
str4 = "------Hello-----"

#List creation
l = ["Hello","world","Its","Me"]

print()

# length of string
print("Length of "+str1+" : "+str(len(str1)))
print("Length of "+str2+" : "+str(len(str2)))
print()

# count function
print("Count of word hello in "+str1+" : "+str(str1.count("hello",0,len(str1))))
print("Count of word hello in "+str2+" : "+str(str2.count("hello",0,len(str2))))
print()

# Center alignment
print("Center aligned text")
print()
print(str1.center(50," "))
print(str2.center(50," "))
print()

# Left alignment
print("Left aligned text")
print()
print(str1.ljust(50," "))
print(str2.ljust(50," "))
print()

# Right alignment
print("Right aligned text")
print()
print(str1.rjust(50," "))
print(str2.rjust(50," "))
print()

# join() 
print("List before joining : "+str(l))
print("Text after joining list : "+"-".join(l))
print()

#isfunc
print(str1+" isalpha ? --- "+str(str1.isalpha()))
print(str1+" isalnum ? --- "+str(str1.isalnum()))
print(str1+" isspace ? --- "+str(str1.isspace()))
print(str1+" isupper ? --- "+str(str1.isupper()))
print(str1+" islower ? --- "+str(str1.islower()))

print()

print(str2+" isalpha ? --- "+str(str2.isalpha()))
print(str2+" isalnum ? --- "+str(str2.isalnum()))
print(str2+" isspace ? --- "+str(str2.isspace()))
print(str2+" isupper ? --- "+str(str2.isupper()))
print(str2+" islower ? --- "+str(str2.islower()))

print()

print(str3+" isalpha ? --- "+str(str3.isalpha()))
print(str3+" isalnum ? --- "+str(str3.isalnum()))
print(str3+" isspace ? --- "+str(str3.isspace()))
print(str3+" isupper ? --- "+str(str3.isupper()))
print(str3+" islower ? --- "+str(str3.islower()))

print()

# find()
print("find 'hello' in "+str1+" : "+str(str1.find('hello',0,len(str1))))
print("find 'hello' in "+str2+" : "+str(str2.find('hello',0,len(str2))))
print()

# rfind
print("rfind 'hello' in "+str1+" : "+str(str1.rfind('hello',0,len(str1))))
print("rfind 'hello' in "+str2+" : "+str(str2.rfind('hello',0,len(str2))))

print()

# startswith 
if (str1.startswith(str2)) :
    print(str1+" starts with "+str2)
else:
    print(str1+" doesn't start with "+str2)

print()

if (str1.startswith(str3)) :
    print(str1+" starts with "+str3)
else:
    print(str1+" doesn't start with "+str3)

print()

# endswith 
if (str1.endswith(str2)):
    print(str1+" ends with "+str2)
else : 
    print(str1+" doesn't end with "+str2)
    
print()

if (str1.endswith(str3)):
    print(str1+" ends with "+str3)
else : 
    print(str1+" doesn't end with "+str3)

print()

# cases
# to upper
print(str1+ " to upper : "+str1.upper())
print(str2+ " to upper : "+str2.upper())

print()

# to lower
print(str1+" to lower :  "+str1.lower())
print(str2+" to lower : "+str2.lower())

print()

# title
print(str1+" to title : "+str1.title())
print(str2+" to title : "+str2.title())

print()

#swapcase
print(str1+" swapcase : "+str1.swapcase())
print(str2+" swapcase : "+str2.swapcase())

print()

#strip
print(str4+" after strip : "+str4.strip("-"))
print(str4+" after lstrip : "+str4.lstrip("-"))
print(str4+" after rstrip : "+str4.rstrip("-"))

print()

#min
print(str1+" - smallest letter : "+str(min(str1)))
print(str2+" - smallest letter : "+str(min(str2)))
print(str3+" - smallest letter : "+str(min(str3)))
print(str4+" - smallest letter : "+str(min(str4)))

print()

#max
print(str1+" - largest letter : "+str(max(str1)))
print(str2+" - largest letter : "+str(max(str2)))
print(str3+" - largest letter : "+str(max(str3)))
print(str4+" - largest letter : "+str(max(str4)))

print()








