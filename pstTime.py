from datetime import datetime
from pytz import timezone

def get_pst_time():
    now_utc = datetime.now(timezone('UTC'))
    time_return = str(now_utc.astimezone(timezone('US/Pacific')))[10:19]
    return time_return

if __name__ == "__main__":
    get_pst_time()