import datetime

def date_time():
    x = datetime.datetime.now()
    AM_PM = (x.strftime("%p"))
    DoY = (x.strftime("%j"))
    HOUR = (x.strftime("%I"))
    MIN = (x.strftime("%M"))
    SEC = (x.strftime("%S"))
    print(HOUR,MIN,SEC,AM_PM)
date_time()