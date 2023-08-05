h = input("Enter your height in inches: ")
w = input("Enter your weight in pounds: ")
h = float(h)
w = float(w)
bmi = round((w/(h*h))*703,2)
print("*"*50)
print(f"Your BMI is {bmi}")
if(bmi >= 39.9):
    print(f"Your BMI of {bmi} is considered Morbidly obese")
elif(bmi >=35 and bmi <= 39.9):
    print(f"Your BMI of {bmi} is considered Severely obese")
elif(bmi >=30 and bmi <= 34.9):
    print(f"Your BMI of {bmi} is considered Moderately obese")
elif(bmi >=25 and bmi <= 29.9):
    print(f"Your BMI of {bmi} is considered Overweight")
elif(bmi >=18.5 and bmi <= 24.9):
    print(f"Your BMI of {bmi} is considered Normal")
elif(bmi >= 16.0 and bmi < 18.5):
    print(f"Your BMI of {bmi} is considered Underweight")
else:
    print(f"Your BMI of {bmi} is considered Severely underweight")