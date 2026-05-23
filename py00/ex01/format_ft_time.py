import datetime as dt
import time

nombre = "agustin"

init_date = dt.datetime.fromtimestamp(0, tz=dt.timezone.utc)
today = dt.datetime.now(dt.timezone.utc)
diference = (today - init_date).total_seconds()

output_1 = f"Seconds since {init_date.strftime('%B %d, %Y')}: {diference:,.4f} or {diference:.2e} in in scientific notation"
output_2 = today.strftime('%b %d %Y')
print(output_1)
print(output_2)
