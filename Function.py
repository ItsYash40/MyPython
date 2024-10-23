# # We can get avg by this process...
# a= 34
# b=45
# c=67

# avg= (a+b+c)/3
# print(avg)

# # now, for long program we take inputs & get the avg by using function,...
# def avg():
#     a=int(input("Enter first element: "))
#     b=int(input("Enter second element: "))
#     c=int(input("Enter third element: "))

#     average=(a+b+c)/3
#     print(average)

# avg()    
# avg() # It can call multiple times


# Function with arguments
def Hi(name, game):
    print("Good morning "+ name+" mostly play" +game)
    return "Thank You"

a= Hi("Yash","PUBG")
print(a)

# Default argument in function call

def goodDay(name, add="Thank You"):
    print(f"Good Day, {name}")
    print(add)

goodDay("Yash", "Thanks") # here the add portion is present, so, it print "Thanks"
goodDay("Python")    # if there is no add(additional part) the it will print default one ,=> add="Thank You" 