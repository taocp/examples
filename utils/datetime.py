import datetime

# 2019-03-12 20:22:00
# 2019-03-13 22:22:00
(datetime.datetime(2019,3,13,22,22,0) - datetime.datetime(2019,3,12,20,22,0)).total_seconds()


datetime.datetime(2019,3,12,20,22,0) + datetime.timedelta(seconds=93600)
