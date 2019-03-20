# Date: 2019-03-19 下午 10:11
import datetime

def utc_local(utc_time):
    UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
    utcTime = datetime.datetime.strptime(utc_time, UTC_FORMAT)
    localtime = utcTime + datetime.timedelta(hours=8)
    return localtime

