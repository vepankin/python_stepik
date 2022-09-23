from datetime import datetime, timedelta

def fill_up_missing_dates(dates):
    dtl = [datetime.strptime(dt, '%d.%m.%Y') for dt in dates]
    dt1 = min(dtl)
    dt2 = max(dtl)
    n = (dt2-dt1).days
    return [(dt1 + timedelta(days=i)).strftime('%d.%m.%Y') for i in range(n + 1)]


dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(dates))
