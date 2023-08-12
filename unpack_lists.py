users = ['admin', 'eric','male',36]
role, name, age, gender = users
print("Incorrect list - in order of role, name,age n gender")
print(role,name,age,gender)
print("Corrected list - in order of role, name,age n gender")

nage,ngender = gender,age
print(role,name,nage,ngender)

print("Just role with other details - ")
r, *others = users
print(r,others)



