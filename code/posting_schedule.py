import os
import time
import cv2
import pathlib
import sys
from datetime import datetime
from random import randrange, uniform
from publish_on_tap import Publish_on_tap


# Paths to Files
# --------------------------------------
# path_project = os.getcwd()
path_video_used                     = '/home/higo/Dev/default_influencer_creator/video_backup/used'
#path_lista_videos_para_publicar     = '/home/higo/Dev/default_influencer_creator/video_backup/to_publish'

#/home/higo/Dev/default_influencer_creator/video_backup/to_publish/6_28-1-2024_18-14-28

path_topic_dicas_de_beleza  = '/home/higo/Dev/default_influencer_creator/content_by_topic/dicas_de_beleza'
path_topic_insp_casamento   = '/home/higo/Dev/default_influencer_creator/content_by_topic/insp_casamento'
path_topic_insp_unhas       = '/home/higo/Dev/default_influencer_creator/content_by_topic/insp_unhas'
path_topic_make             = '/home/higo/Dev/default_influencer_creator/content_by_topic/make'



def select_publica_remove_video(path_topic):

    # Seleciona -> Publica -> Move ou Apaga : Video

    name_file = ''

    #print(' |   get_path_dir_video()')                

    # topic/dir/video.mp4
    list_topic_dir = os.listdir(path_topic)
    poxis_dir_video = randrange(len(list_topic_dir))

    name_dir = list_topic_dir[poxis_dir_video]

    path_dir_video = path_topic + '/' + name_dir

    #print('     path video')
    #print(path_dir_video)

    files_of_dir_videos = os.listdir(path_dir_video)


    for x in files_of_dir_videos:
        if '.mp4' in x and not '.jpg' in x:
            name_file = x

    full_path_video = path_dir_video + '/' + name_file

    print('\n')
    print('     ','Name File')
    print('     ',name_file)

    print('     ','Name Dir')
    print('     ',name_dir)

    print('     ','Path Topic')
    print('     ',path_topic)

    print('     ','Path Dir Video')
    print('     ',path_dir_video)

    print('     ','Full Path Video')
    print('     ',full_path_video)
    print('\n')

    #print('   [ Falta Implementar: Adaptar Publicacao se Preciso ]')

    class_publish = Publish_on_tap()

    class_publish.publish_reels(full_path_video, name_file)

    #print('   >>','Publica no Story')    
    #class_publish.publish_story(full_path_video, name_file)


    # Mover Dir Video para Dir Usado
    cmd = 'mv ' + path_dir_video + ' ' + path_video_used
    time. sleep(2)
    os.system(cmd)


# Postar
# --------------------------------------
def publish_by_topic(topic):

    #print(' |   publish_by_topic(topic)')

    if topic == 'dicas_de_beleza':        
        print(' |   Vamos Publicar Dicas de Beleza')                
        select_publica_remove_video(path_topic_dicas_de_beleza)

    elif topic == 'insp_unhas':
        print(' |   Vamos Publicar Unhas')                
        select_publica_remove_video(path_topic_insp_casamento)

    elif topic == 'insp_casamento':
        print(' |   Vamos Publicar Casamento')                
        select_publica_remove_video(path_topic_insp_unhas)

    elif topic == 'make':
        print(' |   Vamos Publicar Make')                
        select_publica_remove_video(path_topic_make)



def trocar_perfil(perfil):

    # Abrir Instagram App
    cmd = 'adb shell input tap 350 250'
    os.system(cmd)
    time. sleep(2)

    print(' |   ')
    print(' |   ')
    print(' |   Trocando de Perfil')

    #print('     Precisa criar inteligencia para trocar direto')

    # Abrir Opcoes de Perfil
    cmd = 'adb shell input swipe 970 2060 970 2060 600'
    os.system(cmd)
    time. sleep(2)

    # Rolar para o Fim
    cmd = 'adb shell input swipe 600 1600 600 1110'
    os.system(cmd)
    time. sleep(2)

    # Seleciona Ultimo
    cmd = 'adb shell input tap 130 1800' #
    os.system(cmd)
    time. sleep(4)


    # Open botao Recentes
    cmd = 'adb shell input tap 850 2200'
    os.system(cmd)
    time. sleep(2)
    # Fechar Instagram
    cmd = 'adb shell input swipe 500 1200 500 700'
    os.system(cmd)
    time. sleep(2)


    # Stop Instagram
    #cmd = 'adb shell pm clear com.instagram.android'
    #os.system(cmd)
    #time. sleep(2)


    '''
    for x in range(4):

        # Abrir Opcoes de Perfil
        cmd = 'adb shell input swipe 970 2060 970 2060 600'
        os.system(cmd)
        time. sleep(2)

        # Rolar para o Fim
        cmd = 'adb shell input swipe 600 1600 600 1110'
        os.system(cmd)
        time. sleep(2)

       # Seleciona Ultimo
        cmd = 'adb shell input tap 130 1800' #
        os.system(cmd)
        time. sleep(4)
    '''

    print(' |   Perfil trocado')

    # Encerra Instagram


def terca(hh):

        if hh == 1:
            print('>> Domingo 8h')
            print('>> Topico x')
            publish_by_topic('name_topic_1')

        elif hh == 3:
            print('   >> Domingo 12h')
            print('   >> Topico y')
            publish_by_topic('name_topic_1')

        elif hh == 5:
            print('>> Domingo 19h')
            print('Topico z')
            publish_by_topic('name_topic_1')

        elif hh == 6:
            print('>> Domingo 19h')
            print('Topico z')
            publish_by_topic('name_topic_1')

        elif hh == 8:
            print('  | Segunda 8h')
            publish_by_topic('name_topic_1')

        elif hh == 10:
            print('>> Domingo 19h')
            print('Topico z')
            publish_by_topic('name_topic_1')

        elif hh == 12:
            print('>> Segunda 12h')
            print('Topico z')
            publish_by_topic('name_topic_1')

        elif hh == 21:
            print(' |   Quarta 21h')
            print(' |   ')

            trocar_perfil('vibebelezamanaus')
            publish_by_topic('dicas_de_beleza')
            print(' |   Publicacao Concluida')  

            trocar_perfil('sounhas')
            publish_by_topic('insp_unhas')
            print(' |   Publicacao Concluida')  

            trocar_perfil('casamento')
            publish_by_topic('insp_casamento')
            print(' |   Publicacao Concluida')  

        elif hh == 22:
            print('>> Domingo 22h')
            print('Topico d')
            publish_by_topic('name_topic_1')



# Cronograma
# --------------------------------------
def cronograma_publish():

    # 06:00 # 11:00 # 16:00 # 22:00

    currentDateAndTime = datetime.now()
    mm      = currentDateAndTime.minute
    hh      = currentDateAndTime.hour
    dd      = currentDateAndTime.day 
    weekday = currentDateAndTime.weekday()

    if(weekday == 0):
        print('Segunda')

        if hh == 1:
            print('>> Domingo 8h')
            print('>> Topico x')
            publish_by_topic('name_topic_1')

        elif hh == 3:
            print('   >> Domingo 12h')
            print('   >> Topico y')
            publish_by_topic('name_topic_1')

        elif hh == 5:
            print('>> Domingo 19h')
            print('Topico z')
            publish_by_topic('name_topic_1')

        elif hh == 6:
            print('>> Domingo 19h')
            print('Topico z')
            publish_by_topic('name_topic_1')

        elif hh == 8:
            print('  | Segunda 8h')
            publish_by_topic('name_topic_1')

        elif hh == 10:
            print('>> Domingo 19h')
            print('Topico z')
            publish_by_topic('name_topic_1')

        elif hh == 12:
            print('>> Segunda 12h')
            print('Topico z')
            publish_by_topic('name_topic_1')

        elif hh == 22:
            print('>> Domingo 22h')
            print('Topico d')
            publish_by_topic('name_topic_1')

    elif(weekday == 1):
        print(' |   Terca')

        terca(hh)

    elif(weekday == 2):
        print(' |   Quarta')
        terca(hh)

    elif(weekday == 3):
        print('Quinta')

    elif(weekday == 4):
        print('Sexta')

    elif(weekday == 5):
        print('Sabado')

    elif(weekday == 6):

        if hh == 8:
            print('>> Domingo 8h')
            print('>> Topico x')
            publish_by_topic('name_topic_1')

        elif hh == 11:
            print('   >> Domingo 12h')
            print('   >> Topico y')
            publish_by_topic('name_topic_1')

        elif hh == 19:
            print('>> Domingo 19h')
            print('Topico z')
            publish_by_topic('name_topic_1')

        elif hh == 22:
            print('>> Domingo 22h')
            print('Topico d')
            publish_by_topic('name_topic_1')



#trocar_perfil()
cronograma_publish()
