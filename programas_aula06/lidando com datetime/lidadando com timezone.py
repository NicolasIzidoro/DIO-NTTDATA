from datetime import datetime
import pytz 

dt = datetime.now(pytz.timezone('Europe/Oslo'))

print(dt)