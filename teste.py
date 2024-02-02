import os
import time
from datetime import datetime, timedelta


data = datetime.now()

data_str = str(data.day) + '-' + str(data.month) + '-' + str(data.year) + '_' + str(data.hour) + '-' + str(data.minute) + '-' + str(data.second) + '_' + ind

print(data_str)

