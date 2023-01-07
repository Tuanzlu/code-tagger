import time
from datetime import datetime

def get_now_time():
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    return dt_string

if __name__ == "__main__":
    print(get_now_time())
