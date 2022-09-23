from datetime import datetime, timedelta

pattern = '%d.%m.Y%'
dt = datetime.strptime('20.12.2021', pattern)
print(dt.strftime(pattern))

# for d in range(2,11):
#    print((dt + timedelta(days=d)).strftime(pattern))