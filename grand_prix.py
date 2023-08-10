drivers = ["Hamilton", "Versappen", "Vettel", "Leclerc", "Bottas", "Sainz"]

drivers[1]=("Verstappen")
drivers.append("Esteban")
others=["Blue","Elton","Colt"]
drivers.extend(others)
drivers.pop()
drivers.pop(0)
last = drivers.pop(0)
drivers.append(last)
drivers.remove("Blue")
drivers.remove("Elton")
drivers.insert(2,"Elton")
podium=drivers[:3] 

for i in range(len(drivers)):
    print(f"{i+1}. {drivers[i]} ")

print(drivers)
print(podium)