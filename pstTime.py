from datetime import datetime
from pytz import timezone

def get_pst_time(input_variable):
    if input_variable == 'full':
        now_utc = datetime.now(timezone('UTC'))
        time_return = str(now_utc.astimezone(timezone('US/Pacific')))
    elif input_variable == 'partial':
        now_utc = datetime.now(timezone('UTC'))
        time_return = str(now_utc.astimezone(timezone('US/Pacific')))[10:19]
    return time_return

def get_utc_time():
    now_utc = datetime.now(timezone('UTC'))
    time_return = str(now_utc)[10:19]
    return time_return

if __name__ == "__main__":
    test = get_pst_time('full')
    test2 = get_utc_time()

    print(test, test2)