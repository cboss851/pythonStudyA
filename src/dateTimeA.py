from datetime import date,timedelta,datetime
seeDay = date(2017,10,1)
seeDay100 = seeDay + timedelta(days=100)
print(timedelta(days=100))
print("相识",seeDay)
print("相识第100天",seeDay100)

day100 = timedelta(days=100)
seeDay100B = seeDay + day100
print("相识第100天",seeDay100B,"第二种方法")

seeDay = date(2017,10,1)
seeDay2 = date(2017,10,2)
print(seeDay2 - seeDay)
print(type(seeDay2 - seeDay))





