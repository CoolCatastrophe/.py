print("*"*50)
tweet = input("Enter your your tweet: ")
length=len(tweet)
if(length == 250 ):
    print ("The 250 character tweet will work")
elif (length > 250):
    print (f"The {length} character/s long tweet is {length-250} characters too long")
else:
    print(f"The  {length} character/s long tweet will work")
print("*"*50)   