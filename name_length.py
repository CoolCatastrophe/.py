first = input("Enter your first name: ")
last = input("Enter your last name :")
name = first +" "+ last

print("*"*50)
if(len(name) == 12):
    print (f"{name} is exactly the length of average American Name")
elif(len(name) > 12):
    print (f"{name} is longer than the average American Name")
else:
    print (f"{name} is shorter than the average American Name")
print("*"*50)