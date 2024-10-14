# Question 1
name = input("Enter your name: ")
print(f"Good Morning  {name}")

# Question 2
letter = '''Dear   <|Name|>,
you are selected 
on date <|Date|>'''

print(letter.replace(" <|Name|>", "Yash").replace("<|Date|>", "13 July 2026"))  #Channing Process

# Question 3 (find the double space in string)
name = " Yash is very good  gamer"
print(name.find("  ")) # if return -1, there are no double space "  "

#Question 4
str1= "Hi Yash,\n \tPlease tell me \nhow can I help you?"
print(str1)

