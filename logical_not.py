from datetime import datetime
year = input("What year were you born in?")

if not year.isnumeric():
    input("That isnt a number.Please Try Again!")
else:
    year=int(year)
    current_year = datetime.now().year
    print(f"You were born {current_year-year} years ago")

