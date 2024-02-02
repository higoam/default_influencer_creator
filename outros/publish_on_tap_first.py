import os
import time
from datetime import datetime, timedelta

# Escolher Video
#def publish():


# Postar
def publish():

    path_origem = '/home/higo/Dev/krossy/vibebelezamanaus/downloaded_media/3266573476545880415/boutique_danath_3266573476545880415.mp4'
    path_destino = '/sdcard/Download'

    # Copiar Video para Celular
    cmd = 'adb push ' + path_origem + ' ' + path_destino
    print(cmd)
    os.system(cmd)

    # Entrar em File App
    cmd = 'adb shell input tap 175 250'
    time. sleep(2)
    os.system(cmd)

    # Entrar no Dir Download, Preciso disso pra enchergar o novo video
    cmd = 'adb shell input tap 300 1300'
    time. sleep(2)
    os.system(cmd)

    # Open botao home, verifica nome
    cmd = 'adb shell input tap 850 2200'
    time. sleep(2)
    os.system(cmd)

    # Fechar File App
    cmd = 'adb shell input swipe 500 1200 500 700'
    time. sleep(2)
    os.system(cmd)

    # Abrir Instagram App
    cmd = 'adb shell input tap 350 250'
    time. sleep(2)
    os.system(cmd)

    # TIME to UPDATE
    time. sleep(8)

    # Click - Botao Add Puplicacao +
    cmd = 'adb shell input tap 500 2000'
    time. sleep(2)
    os.system(cmd)

    # Click - Escolher RELL
    cmd = 'adb shell input tap 950 1950'
    time. sleep(2)
    os.system(cmd)

    # Click - Aba com opcaoes de dir
    cmd = 'adb shell input tap 230 730'
    time. sleep(2)
    os.system(cmd)

    # Click - Escolher Grade de Recentes
    cmd = 'adb shell input tap 200 1000'
    time. sleep(2)
    os.system(cmd)

    # Click - Escolher Primeiro Video da Grade
    cmd = 'adb shell input tap 175 1100'
    time. sleep(2)
    os.system(cmd)

    # Next
    time.sleep(2)
    cmd = 'adb shell input tap 950 2000'
    os.system(cmd)

    # Subir Video para Aparecer Todas Opcoes
    time.sleep(2)
    cmd = 'adb shell input swipe 500 1500 500 800'
    os.system(cmd)

    # Add Msg
    time.sleep(2)
    cmd = 'adb shell input tap 200 700'
    os.system(cmd)
    time.sleep(2)    
    cmd = 'adb shell input text \'\#vibebelezamanaus%s\#manaus \''
    os.system(cmd)



    # Recua teclado 1

    # Recua teclado 2

    # Add Topics

    # Add Location

    # Click Compartilhar
    time.sleep(2)
    cmd = 'adb shell input tap 800 2000'
    os.system(cmd)

    # TIME to UPLOAD
    time. sleep(15)


    # Open botao home, verifica nome
    cmd = 'adb shell input tap 850 2200'
    time. sleep(2)
    os.system(cmd)

    # Fechar File App
    cmd = 'adb shell input swipe 500 1200 500 700'
    time. sleep(2)
    os.system(cmd)


publish()