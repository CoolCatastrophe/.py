lando_2023_results = [4,3,5,8,3,5,5,5,3,4,14,10,2,7,7,8,10,10,9,10,7]

total = 0
avg=0
for position in lando_2023_results:
    total+=position
avg=total/len(lando_2023_results)
print(total,avg)

#to find lowest number in lando_2023_results
low=lando_2023_results[0]
for i in lando_2023_results:
    if i<low:
        low=i
print(low)


#to find index of low in lando_2023_results
for i in range(len(lando_2023_results)):
    if lando_2023_results[i]==low:
        print(i)