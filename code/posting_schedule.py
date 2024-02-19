import os
import time
import cv2
import pathlib
import sys
from datetime import datetime
from random import randrange, uniform

#from publish_on_tap import Publish_on_tap
from publish_on_tap import publish_reels
from publish_on_tap import publish_story

# Paths to Files
# --------------------------------------
# path_project = os.getcwd()
#path_video_used             = '/home/higo/Dev/default_influencer_creator/video_backup/used'

path_topic_dicas_de_beleza  = '/home/higo/Dev/default_influencer_creator/medias_to_post/dicas_beleza'
path_topic_unhas_decoracao  = '/home/higo/Dev/default_influencer_creator/medias_to_post/unhas_decoracao'
path_topic_insp_bebe        = '/home/higo/Dev/default_influencer_creator/medias_to_post/bebe'
path_topic_insp_petts       = '/home/higo/Dev/default_influencer_creator/medias_to_post/petts'

path_topic_insp_casamento   = '/home/higo/Dev/medias_to_post'
path_topic_make             = '/home/higo/Dev/default_influencer_creator/content_by_topic/make'


def select_publica_remove_video(path_topic):

    name_file = ''

    path_available_medias = path_topic + '/available'

    list_available_medias = os.listdir(path_available_medias)
    index_selected_media = randrange(len(list_available_medias)) 

    name_media_selected = list_available_medias[index_selected_media]
    full_path_selected = path_available_medias + '/' + name_media_selected

    path_reel  = full_path_selected + '/reel'
    path_story_video = full_path_selected + '/story_video'

    print(path_reel)
    print(path_story_video)

    publish_reels(path_reel)
    publish_story(path_story_video)

    # Entrar no Dir Download, Preciso disso pra enchergar o novo video
    print(' |   Move dir to USED')
    cmd = 'mv ' + full_path_selected + ' ' + path_topic + '/used' 
    os.system(cmd)
    time. sleep(2)


def pause_system(hora):

    print(' |   Pause System')

    hh_now = hora

    while(hora == hh_now):

        time_now = datetime.now()

        mm_now = time_now.minute
        hh_now = time_now.hour

        if mm_now < 10:

            limite_date = datetime(time_now.year, time_now.month, time_now.day, time_now.hour, 9, 59, 999999)
            delta = limite_date - time_now
            print('')
            print(' |   Time Limite :  ',limite_date)
            print(' |   Time Now    :  ',time_now)
            print(' |   Min < 10')
            print(' |   Diff Click Home:  ',delta)
            print(' |   Diff Click Home:  ',delta.seconds)
            print(' |   Aplicando Soneca: ',delta.seconds)    
            time. sleep(delta.seconds + 2)

            print(' |   Touch Home')
            cmd = 'adb shell input tap 540 2200'
            os.system(cmd)

        elif mm_now < 20:

            limite_date = datetime(time_now.year, time_now.month, time_now.day, time_now.hour, 19, 59, 999999)
            delta = limite_date - time_now
            print('')
            print(' |   Time Limite :  ',limite_date)
            print(' |   Time Now    :  ',time_now)
            print(' |   Min < 20')
            print(' |   Diff Click Home:  ',delta)
            print(' |   Diff Click Home:  ',delta.seconds)
            print(' |   Aplicando Soneca: ',delta.seconds)    
            time. sleep(delta.seconds + 2)

            print(' |   Touch Home')
            cmd = 'adb shell input tap 540 2200'
            os.system(cmd)

        elif mm_now < 30:

            limite_date = datetime(time_now.year, time_now.month, time_now.day, time_now.hour, 29, 59, 999999)
            delta = limite_date - time_now
            print('')
            print(' |   Time Limite :  ',limite_date)
            print(' |   Time Now    :  ',time_now)
            print(' |   Min < 30')
            print(' |   Diff Click Home:  ',delta)
            print(' |   Diff Click Home:  ',delta.seconds)
            print(' |   Aplicando Soneca: ',delta.seconds)    
            time. sleep(delta.seconds + 2)

            print(' |   Touch Home')
            cmd = 'adb shell input tap 540 2200'
            os.system(cmd)


        elif mm_now < 40:

            limite_date = datetime(time_now.year, time_now.month, time_now.day, time_now.hour, 39, 59, 999999)
            delta = limite_date - time_now
            print('')
            print(' |   Time Limite :  ',limite_date)
            print(' |   Time Now    :  ',time_now)
            print(' |   Min < 40')
            print(' |   Diff Click Home:  ',delta)
            print(' |   Diff Click Home:  ',delta.seconds)
            print(' |   Aplicando Soneca: ',delta.seconds)    
            time. sleep(delta.seconds + 2)

            print(' |   Touch Home')
            cmd = 'adb shell input tap 540 2200'
            os.system(cmd)

        elif mm_now < 50:

            limite_date = datetime(time_now.year, time_now.month, time_now.day, time_now.hour, 49, 59, 999999)
            delta = limite_date - time_now
            print('')
            print(' |   Time Limite :  ',limite_date)
            print(' |   Time Now    :  ',time_now)
            print(' |   Min < 50')
            print(' |   Diff Click Home:  ',delta)
            print(' |   Diff Click Home:  ',delta.seconds)
            print(' |   Aplicando Soneca: ',delta.seconds)    
            time. sleep(delta.seconds + 2)

            print(' |   Touch Home')
            cmd = 'adb shell input tap 540 2200'
            os.system(cmd)

        elif mm_now < 60:

            limite_date = datetime(time_now.year, time_now.month, time_now.day, time_now.hour, 59, 59, 999999)
            delta = limite_date - time_now
            print('')
            print(' |   Time Limite :  ',limite_date)
            print(' |   Time Now    :  ',time_now)
            print(' |   Min < 60')
            print(' |   Diff Click Home:  ',delta)
            print(' |   Diff Click Home:  ',delta.seconds)
            print(' |   Aplicando Soneca: ',delta.seconds)

            hh_now = hh_now + 1  
            time. sleep(delta.seconds + 2)

            print(' |   Touch Home')
            cmd = 'adb shell input tap 540 2200'
            os.system(cmd)



    

    #time. sleep(62)
    #limite_date = datetime.now()

    #print(currentDate)



    '''    
    '''




# Postar
# --------------------------------------
def publish_by_topic(topic):

    #print(' |   publish_by_topic(topic)')

    if topic == 'dicas_de_beleza':        
        print(' |   ')  
        print(' |   Vamos Publicar Dicas de Beleza')                
        select_publica_remove_video(path_topic_dicas_de_beleza)

    elif topic == 'unhas_decoracao':
        print(' |   ')  
        print(' |   Vamos Publicar Unhas')                
        select_publica_remove_video(path_topic_unhas_decoracao)

    elif topic == 'insp_casamento':
        print(' |   ')  
        print(' |   Vamos Publicar Casamento')                
        select_publica_remove_video(path_topic_insp_casamento)

    elif topic == 'make':
        print(' |   ')  
        print(' |   Vamos Publicar Make')                
        select_publica_remove_video(path_topic_make)

    elif topic == 'pet':
        print(' |   ')  
        print(' |   Vamos Publicar Pet')                
        select_publica_remove_video(path_topic_insp_petts)

    elif topic == 'bebe':
        print(' |   ')                
        print(' |   Vamos Publicar Bebe')                
        select_publica_remove_video(path_topic_insp_bebe)

    else:
        print(' |   Falha na Publicacao')  

    print(' |   Publicacao Concluida')  


def trocar_perfil(perfil):

    # Abrir Instagram App
    cmd = 'adb shell input tap 350 250'
    os.system(cmd)
    time. sleep(5)

    print('    ')
    print('    ')
    print(' -------------------------------------')
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


def segunda(hh):

        if   hh == 1:
            print(' |   Segunda ',str(hh),'h')

        elif hh == 3:
            print(' |   Segunda ',str(hh),'h')

        elif hh == 5:
            print(' |   Segunda ',str(hh),'h')
            print(' |   ')

            trocar_perfil('Petts Mimados')
            publish_by_topic('pet')
            print(' |   ')

            trocar_perfil('Nossa Inspiracao Unhas')
            #publish_by_topic('insp_unhas')
            print(' |   ')

            trocar_perfil('Unhas de Fada AM')
            #publish_by_topic('insp_unhas')
            print(' |   ')

            trocar_perfil('Somos Corujas Baby')
            publish_by_topic('bebe')
            print(' |   ')

        elif hh == 6:
            print(' |   Segunda ',str(hh),'h')

        elif hh == 8:
            print(' |   Segunda ',str(hh),'h')

        elif hh == 10:
            print(' |   Segunda ',str(hh),'h')

        elif hh == 12:
            print(' |   Segunda ',str(hh),'h')

        elif hh == 20:
            print(' |   Segunda ',str(hh),'h')

        elif hh == 21:
            print(' |   Segunda ',str(hh),'h')

        elif hh == 22:
            print(' |   Segunda ',str(hh),'h')

        elif hh == 23:
            print(' |   Segunda ',str(hh),'h')

def terca(hh):

        if hh == 1:
            print(' |   Terca ',str(hh),'h')

        elif hh == 3:
            print(' |   Terca ',str(hh),'h')

        elif hh == 5:
            print(' |   Terca ',str(hh),'h')

        elif hh == 6:
            print(' |   Terca ',str(hh),'h')

        elif hh == 8:
            print(' |   Terca ',str(hh),'h')

        elif hh == 10:
            print(' |   Terca ',str(hh),'h')

        elif hh == 12:
            print(' |   Terca ',str(hh),'h')

        elif hh == 20:
            print(' |   Terca ',str(hh),'h')

        elif hh == 21:
            print(' |   Terca ',str(hh),'h')

        elif hh == 23:
            print(' |   Terca ',str(hh),'h')

def quarta(hh):

        if   hh == 1:
            print(' |   Quarta ',str(hh),'h')

        elif hh == 3:
            print(' |   Quarta ',str(hh),'h')

        elif hh == 5:
            print(' |   Quarta ',str(hh),'h')
            print(' |   ')

            trocar_perfil('Petts Mimados')
            publish_by_topic('pet')
            print(' |   ')

            trocar_perfil('Nossa Inspiracao Unhas')
            #publish_by_topic('insp_unhas')
            print(' |   ')

            trocar_perfil('Unhas de Fada AM')
            #publish_by_topic('insp_unhas')
            print(' |   ')

            trocar_perfil('Somos Corujas Baby')
            publish_by_topic('bebe')
            print(' |   ')

        elif hh == 6:
            print(' |   Quarta ',str(hh),'h')

        elif hh == 8:
            print(' |   Quarta ',str(hh),'h')

        elif hh == 10:
            print(' |   Quarta ',str(hh),'h')

        elif hh == 12:
            print(' |   Quarta ',str(hh),'h')

        elif hh == 20:
            print(' |   Quarta ',str(hh),'h')

        elif hh == 22:
            print(' |   Quarta ',str(hh),'h')
            print(' |   ')

            trocar_perfil('Petts Mimados')
            #publish_by_topic('pet')
            print(' |   ')

            trocar_perfil('Nossa Inspiracao Unhas')
            #publish_by_topic('insp_unhas')
            print(' |   ')

            trocar_perfil('Unhas de Fada AM')
            publish_by_topic('unhas_decoracao')
            print(' |   ')

            trocar_perfil('Somos Corujas Baby')
            publish_by_topic('bebe')
            print(' |   ')

def quinta(hh):

        if   hh == 1:
            print('')
            print(' |   Quinta ',str(hh),'h')
            pause_system(hh)

        elif hh == 3:
            print('')
            print(' |   Quinta ',str(hh),'h')
            pause_system(hh)

        elif hh == 5:
            print('')
            print(' |   Quinta ',str(hh),'h')
            pause_system(hh)

        elif hh == 7:
            print('')
            print(' |   Quinta ',str(hh),'h')
            pause_system(hh)

        elif hh == 9:
            print('')
            print(' |   Quinta ',str(hh),'h')
            pause_system(hh)

        elif hh == 11:
            print('')
            print(' |   Quinta ',str(hh),'h')
            pause_system(hh)

        elif hh == 13:
            print('')
            print(' |   Quinta ',str(hh),'h')
            pause_system(hh)

        elif hh == 18:
            print('')
            print(' |   Quinta ',str(hh),'h')
            pause_system(hh)

        elif hh == 19:
            print('')
            print(' |   Quinta ',str(hh),'h')
            pause_system(hh)

        elif hh == 20:
            print('')
            print(' |   Quinta ',str(hh),'h')
            pause_system(hh)

        elif hh == 21:
            print('')
            print(' |   Quinta ',str(hh),'h')
            pause_system(hh)

        elif hh == 22:
            print('')
            print(' |   Quinta ',str(hh),'h')
            pause_system(hh)

        else:
            print('')
            print(' |   Quinta ',str(hh),'h')
            pause_system(hh)

def sexta(hh):

        if   hh == 1:
            print('')
            print(' |   Sexta ',str(hh),'h')
            pause_system(hh)

        elif hh == 5:
            print('')
            print(' |   Sexta ',str(hh),'h')

            trocar_perfil('Petts Mimados')
            publish_by_topic('pet')
            print(' |   ')

            trocar_perfil('Nossa Inspiracao Unhas')
            publish_by_topic('unhas_decoracao')
            print(' |   ')

            trocar_perfil('Unhas de Fada AM')
            publish_by_topic('unhas_decoracao')
            print(' |   ')

            trocar_perfil('Somos Corujas Baby')
            publish_by_topic('bebe')
            print(' |   ')

            pause_system(hh)

        elif hh == 11:
            print('')
            print(' |   Sexta ',str(hh),'h')

            trocar_perfil('Petts Mimados')
            publish_by_topic('pet')
            print(' |   ')

            trocar_perfil('Nossa Inspiracao Unhas')
            publish_by_topic('unhas_decoracao')
            print(' |   ')

            trocar_perfil('Unhas de Fada AM')
            publish_by_topic('unhas_decoracao')
            print(' |   ')

            trocar_perfil('Somos Corujas Baby')
            publish_by_topic('bebe')
            print(' |   ')

            pause_system(hh)

        elif hh == 17:
            print('')
            print(' |   Sexta ',str(hh),'h')

            trocar_perfil('Petts Mimados')
            publish_by_topic('pet')
            print(' |   ')

            trocar_perfil('Nossa Inspiracao Unhas')
            publish_by_topic('unhas_decoracao')
            print(' |   ')

            trocar_perfil('Unhas de Fada AM')
            publish_by_topic('unhas_decoracao')
            print(' |   ')

            trocar_perfil('Somos Corujas Baby')
            publish_by_topic('bebe')
            print(' |   ')

            pause_system(hh)

        elif hh == 20:
            print('')
            print(' |   Sexta ',str(hh),'h')

            trocar_perfil('Petts Mimados')
            publish_by_topic('pet')
            print(' |   ')

            trocar_perfil('Nossa Inspiracao Unhas')
            publish_by_topic('unhas_decoracao')
            print(' |   ')

            trocar_perfil('Unhas de Fada AM')
            publish_by_topic('unhas_decoracao')
            print(' |   ')

            trocar_perfil('Somos Corujas Baby')
            publish_by_topic('bebe')
            print(' |   ')

            pause_system(hh)

        elif hh == 21:
            print('')
            print(' |   Sexta ',str(hh),'h')

            trocar_perfil('Petts Mimados')
            publish_by_topic('pet')
            print(' |   ')

            trocar_perfil('Nossa Inspiracao Unhas')
            publish_by_topic('unhas_decoracao')
            print(' |   ')

            trocar_perfil('Unhas de Fada AM')
            publish_by_topic('unhas_decoracao')
            print(' |   ')

            trocar_perfil('Somos Corujas Baby')
            publish_by_topic('bebe')
            print(' |   ')

            pause_system(hh)

        elif hh == 22:
            print('')
            print(' |   Sexta ',str(hh),'h')

            trocar_perfil('Petts Mimados')
            publish_by_topic('pet')
            print(' |   ')

            trocar_perfil('Nossa Inspiracao Unhas')
            publish_by_topic('unhas_decoracao')
            print(' |   ')

            trocar_perfil('Unhas de Fada AM')
            publish_by_topic('unhas_decoracao')
            print(' |   ')

            trocar_perfil('Somos Corujas Baby')
            publish_by_topic('bebe')
            print(' |   ')

            pause_system(hh)

        elif hh == 23:
            print('')
            print(' |   Sexta ',str(hh),'h')

            trocar_perfil('Petts Mimados')
            publish_by_topic('pet')
            print(' |   ')

            trocar_perfil('Nossa Inspiracao Unhas')
            publish_by_topic('unhas_decoracao')
            print(' |   ')

            trocar_perfil('Unhas de Fada AM')
            publish_by_topic('unhas_decoracao')
            print(' |   ')

            trocar_perfil('Somos Corujas Baby')
            publish_by_topic('bebe')
            print(' |   ')

            pause_system(hh)

        else:
            print('')
            print(' |   Sexta ',str(hh),'h')
            pause_system(hh)

def sabado(hh):

        if   hh == 5:
            print('')
            print(' |   Sabado ',str(hh),'h')
            pause_system(hh)

        if   hh == 11:
            print('')
            print(' |   Sabado ',str(hh),'h')
            pause_system(hh)

        elif hh == 22:
            print(' |   Sabado ',str(hh),'h')

def domingo(hh):

        if   hh == 1:
            print(' |   Domingo ',str(hh),'h')

        elif hh == 3:
            print(' |   Domingo ',str(hh),'h')

        elif hh == 5:
            print(' |   Domingo ',str(hh),'h')
            print(' |   ')

            trocar_perfil('Petts Mimados')
            publish_by_topic('pet')
            print(' |   ')

            trocar_perfil('Nossa Inspiracao Unhas')
            #publish_by_topic('insp_unhas')
            print(' |   ')

            trocar_perfil('Unhas de Fada AM')
            #publish_by_topic('insp_unhas')
            print(' |   ')

            trocar_perfil('Somos Corujas Baby')
            publish_by_topic('bebe')
            print(' |   ')

        elif hh == 6:
            print(' |   Domingo ',str(hh),'h')

        elif hh == 8:
            print(' |   Domingo ',str(hh),'h')

        elif hh == 10:
            print(' |   Domingo ',str(hh),'h')
            trocar_perfil('Petts Mimados')
            publish_by_topic('pet')
            print(' |   ')

            trocar_perfil('Nossa Inspiracao Unhas')
            #publish_by_topic('insp_unhas')
            print(' |   ')

            trocar_perfil('Unhas de Fada AM')
            #publish_by_topic('insp_unhas')
            print(' |   ')

            trocar_perfil('Somos Corujas Baby')
            #publish_by_topic('bebe')
            print(' |   ')

        elif hh == 12:
            print(' |   Domingo ',str(hh),'h')

        elif hh == 20:
            print(' |   Domingo ',str(hh),'h')

        elif hh == 22:
            print(' |   Domingo ',str(hh),'h')


# Cronograma
# --------------------------------------
def cronograma_publish():

    currentDateAndTime = datetime.now()
    mm      = currentDateAndTime.minute
    hh      = currentDateAndTime.hour
    dd      = currentDateAndTime.day 
    weekday = currentDateAndTime.weekday()

    if(  weekday == 0):
        segunda(hh)

    elif(weekday == 1):
        terca(hh)

    elif(weekday == 2):
        quarta(hh)

    elif(weekday == 3):
        quinta(hh)

    elif(weekday == 4):
        sexta(hh)

    elif(weekday == 5):
        sabado(hh)

    elif(weekday == 6):
        domingo(hh)


def start_all():

    while(True):
        cronograma_publish()



start_all()