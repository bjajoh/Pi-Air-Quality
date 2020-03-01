from sds011 import *
from datetime import datetime
import time


def time_now():
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
    return timestampStr

sensor = SDS011("/dev/ttyUSB0")

# Turn-on sensor
sensor.sleep(sleep=False)

# Turn-off sensor
#sensor.sleep(sleep=True)
#
while 1:
    #sensor.sleep(sleep=False)
    #time.sleep(10)
    pmt_2_5, pmt_10 = sensor.query()
    print (time_now(), end='')
    print(f"    PMT2.5: {pmt_2_5} μg/m3    ", end='')
    print(f"PMT10 : {pmt_10} μg/m3")
    #sensor.sleep(sleep=True)
    #time.sleep(2)
