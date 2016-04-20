from datetime import datetime,timedelta,timezone
now = datetime.now() # 获取当前datetime
print(now)
print(type(now))
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)

t = 1429417200.0
print(datetime.fromtimestamp(t))# 本地时间(北京时间为东八区 比格林威治标准时间快8个小时)
print(datetime.utcfromtimestamp(t)) # UTC时间

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
now + timedelta(hours=10)
print(now.strftime('%a, %b %d %H:%M'))


tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
print(now)

dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)