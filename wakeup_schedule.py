import os
import time
import cv2
import pathlib
from datetime import datetime

print(' |   Iniciou Wake UP Schedule: ', datetime.now())

ENABLE_TO_PUBLISH = True
ENABLE_TO_KEEP_ALIVE = True
MINUTE_OF_PUBLICATION = 3

while(True):

    currentDateAndTime = datetime.now()
    mm = currentDateAndTime.minute
    hh = currentDateAndTime.hour

    if ( hh==1 or hh==3 or hh==5 or hh==7 or hh==9 or hh==11 or hh==13 or hh==16 or hh==17 or hh==19 or hh==22 ) and ( ENABLE_TO_PUBLISH==True ):
        #if mm == MINUTE_OF_PUBLICATION:
        if mm<100: #MINUTE_OF_PUBLICATION:
            print(' |   Acordando Cronograma de Publicacao')
            cmd = 'python3 code/posting_schedule.py'
            os.system(cmd)
            print(' |   Adormecendo Cronograma de Publicacao')
            ENABLE_TO_PUBLISH = False

    elif ( hh==2 or hh==4 or hh==6 or hh==8 or hh==10 or hh==12 or hh==14 or hh==17 or hh==18 or hh==20 or hh==23 ):
        ENABLE_TO_PUBLISH = True

    # Modo freedCrug - Nao dormir
    if ( mm==11 or mm==21 or mm==31 or mm==41 or mm==51 ) and ( ENABLE_TO_KEEP_ALIVE==True ):
        print(' |   Touch Home')
        cmd = 'adb shell input tap 540 2200'
        os.system(cmd)
        ENABLE_TO_KEEP_ALIVE=False 

        print(' |   Delay de 8 min')
        time.sleep(480)

    elif ( mm==12 or mm==22 or mm==32 or mm==42 or mm==52 ):
        ENABLE_TO_KEEP_ALIVE = True

