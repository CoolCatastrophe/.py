from textblob import TextBlob
import art as a
import pyttsx3

print(a.text2art("Task Master"))
engine = pyttsx3.init()
engine.setProperty("rate", 300)
engine.say(
    """Helloooo Employee Number 12. We hope you had a great day at work. 
Its time to give your feedback, enter your employee wellness statement"""
)
engine.runAndWait()

print("Enter your statement: ")
phrase = input("> ")
while (TextBlob(phrase).sentiment.polarity) < 0.5:
    engine.say(
        "Employee Number 12, that was not a very positive statement. Try again and be more positive this time. We know how much you love working here."
    )
    print("More positive statement please: ")
    engine.runAndWait()
    phrase = input("> ")
engine.say(
    "Thank you for your feedback employee number 12 for such a kind and positive statement, We here at Task Master appretiate you too."
)
engine.runAndWait()
print("Have a great day!")
