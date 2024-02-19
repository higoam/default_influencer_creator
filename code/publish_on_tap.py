import os
import time
from datetime import datetime, timedelta
from processamento_video import get_durantion_video

def publish_story(path_story):

    print(' |   publish_story()')
    print('')
    print(' |   Listar Arquivos de Story')

    files_of_dir_videos = os.listdir(path_story)
    time. sleep(1)

    for x in files_of_dir_videos:
        print(' |  ',x)

        path_origem = path_story + '/' + x
        path_destino = '/sdcard/Download'

        # Copiar Video para Celular
        print(' |   ')
        print(' |   Copiando Arquivo ', x ,' para Celular')
        print(' |----------------------------------------------')
        cmd = 'adb push ' + path_origem + ' ' + path_destino
        print(cmd)
        os.system(cmd)
        print(' |----------------------------------------------')

        print(' |   Abrir Gerenciador de Arquivos')
        cmd = 'adb shell input tap 940 250'
        os.system(cmd)
        time. sleep(4)

        print(' |   Selecionar Download')
        cmd = 'adb shell input tap 550 450'
        os.system(cmd)
        time. sleep(2)

        print(' |   Selecionar Arquivo 1')
        cmd = 'adb shell input tap 400 540'
        os.system(cmd)
        time. sleep(2)

        print(' |   Clicar em Compartilhar')
        cmd = 'adb shell input tap 150 2040'
        os.system(cmd)
        time. sleep(2)

        print(' |   Rolada pra cima 1')
        cmd = 'adb shell input swipe 500 1900 500 200'
        os.system(cmd)
        time. sleep(5)

        print(' |   Selecionar Stories')
        cmd = 'adb shell input tap 700 1200'
        os.system(cmd)
        time. sleep(2)

        print(' |   Foi para Instagram')
        print(' |   Tempo para Abrir Instagram')
        time. sleep(10)

        print(' |   Clicar em Seu Story')
        cmd = 'adb shell input tap 250 1930'
        os.system(cmd)
        time. sleep(2)

        print(' |   Tempo para Subir Story')                
        time.sleep(30)

        print(' |   Fechar Instagram e Gerenciador de Arquivo')
        cmd = 'adb shell input tap 850 2200'
        os.system(cmd)
        time. sleep(2)
        cmd = 'adb shell input swipe 500 1200 500 700'
        os.system(cmd)
        time. sleep(2)
        cmd = 'adb shell input swipe 500 1200 500 700'
        os.system(cmd)
        time. sleep(2)

        # Apagar Download
        print(' |   Apagar Download')
        cmd = 'adb shell rm \'/sdcard/Download/*\''
        os.system(cmd)
        time.sleep(2)


def publish_reels(path_reel):

    print(' |   publish_reels()')

    list_reels = os.listdir(path_reel)
    name_reel = list_reels[0]
   
    path_origem = path_reel + '/' + name_reel
    path_destino = '/sdcard/Download'

    # Copiar Video para Celular
    print(' |   ')
    print(' |   Copiando Arquivos para Celular')
    print(' |----------------------------------------------')
    cmd = 'adb push ' + path_origem + ' ' + path_destino
    print(cmd)
    os.system(cmd)
    print(' |----------------------------------------------')

    print(' |   Abrir Gerenciador de Arquivos')
    cmd = 'adb shell input tap 940 250'
    os.system(cmd)
    time. sleep(2)

    print(' |   Selecionar Download')
    cmd = 'adb shell input tap 550 450'
    os.system(cmd)
    time. sleep(2)

    print(' |   Selecionar Arquivo 1')
    cmd = 'adb shell input tap 400 540'
    os.system(cmd)
    time. sleep(2)

    print(' |   Clicar em Compartilhar')
    cmd = 'adb shell input tap 150 2040'
    os.system(cmd)
    time. sleep(2)

    print(' |   Rolada pra cima 1')
    cmd = 'adb shell input swipe 500 1900 500 200'
    os.system(cmd)
    time. sleep(3)

    print(' |   Selecionar Reels')
    cmd = 'adb shell input tap 950 1200'
    os.system(cmd)
    time. sleep(2)

    print(' |   Foi para Instagram')
    print(' |   Tempo para Abrir Instagram')
    time. sleep(7)

    print(' |   Clicar em Avancar')
    cmd = 'adb shell input tap 900 2000'
    os.system(cmd)
    time. sleep(2)
    
    print(' |   Rolar Para cima')                
    cmd = 'adb shell input swipe 500 1500 500 800'
    os.system(cmd)
    time.sleep(2)

    print('Add Dados')

    print(' |   Compartilhar Video')
    cmd = 'adb shell input tap 800 2000'
    os.system(cmd)
    time.sleep(2)

    print(' |   Iniciando Upload Video')
    time. sleep(30)
    print(' |   Uploading Video')
    time. sleep(30)

    print(' |   Fechar Instagram e Gerenciador de Arquivos')
    cmd = 'adb shell input tap 850 2200'
    os.system(cmd)
    time. sleep(2)
    cmd = 'adb shell input swipe 500 1200 500 700'
    os.system(cmd)
    time. sleep(2)
    cmd = 'adb shell input swipe 500 1200 500 700'
    os.system(cmd)
    time. sleep(2)

    print(' |   Apagar Download')
    cmd = 'adb shell rm \'/sdcard/Download/*\''
    os.system(cmd)
    time.sleep(2)
