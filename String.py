print(" Hello Yash")
name= " Yash "  #String
print(name)

nameshort= name[0:3] #Start from 0 still length 2. 
print(nameshort)

character2= name[2]  # to print specific character
print(character2)

print(name[-3:-1]) #Print from the -ve index 
print(name[1:3])

print(name[:4]) # is same as print(name[0:4])

c= "dairymilk"
print(c[1:8:3]) #At first it will take index1 to index 8(airymil). Then print the letters with gap 3 =>(ayl)

print(len(c)) # for define the length 
print(c.endswith("milk")) # String is end with "ilk" or not ? if yes => true (boolean)
print(c.startswith("Dai")) #String is Start with "Dai" or not ? if no => False (boolean) // Case sensative

d ="My India "
index= d.find("India")
print(index)

e=" Hi, \"Welcome\" to\n my \t home" #\n -> for new line. \t-> for space, \"\"" -> for double quote
print(e)

f1 = "Python is a Compiled Language."  # for replace word
print(f1.replace("Compiled", "Interpreted"))

str1 = "He's name is Yash.  Yash play PUBG very well." # for capitalizes each staring letter in word
print(str1.title())

