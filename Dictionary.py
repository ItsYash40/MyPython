marks={"Yash": 100,
       "Sneha": 90,
        "Allen": 30 }

print(marks,type(marks)) # for display the marks
print(marks["Yash"])  # mark on specific name

# METHODS 
print(marks.keys()) # print the key items( left side items)
print(marks.values()) #print the values items( right side items)
marks.update({"Nobita": 99, "Sizuka": 80}) #Update data in Dictionary
print(marks)

print(marks.get("Sneha")) #to get data 
print(marks.pop("Allen"))