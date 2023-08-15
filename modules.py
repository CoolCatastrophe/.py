import calendar as c, datetime as dt
 
print(c.isleap(2000))


def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(leap_year(4))

print(c.weekday(2002, 7, 24))
print(dt.datetime.now())