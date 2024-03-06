from datetime import datetime

request_time= 1705795200000

last_date_in_db = datetime.fromtimestamp(request_time/1000).strftime("%Y-%m-%d")
last_date_in_db_full = datetime.fromtimestamp(request_time/1000).isoformat()

print(last_date_in_db_full)