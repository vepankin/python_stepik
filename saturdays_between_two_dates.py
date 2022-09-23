from datetime import date

# def saturdays_between_two_dates(date1, date2):
#    return len([1 for x in range(min(date1, date2).toordinal(), max(date1, date2).toordinal() + 1) if date.fromordinal(x).weekday() == 5])

def saturdays_between_two_dates(date1, date2):
    if date1 > date2:
        date1, date2 = date2, date1
    return len([1 for x in range(date1.toordinal(), date2.toordinal() + 1) if date.fromordinal(x).weekday() == 5])

date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))