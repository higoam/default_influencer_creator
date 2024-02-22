# 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

import os
import time
from datetime import datetime, timedelta

from processamento_video import break_video_to_story

path_base = os.getcwd()
print(path_base)

point_to_new_media =    path_base + '/../point_to_new_media'
z_new_media =           path_base + '/../medias_to_post/z_new_medias'

#path_topic_dicas_de_beleza  = '/home/higo/Dev/medias_to_post/dicas_beleza/available'
#path_topic_insp_unhas       = '/home/higo/Dev/medias_to_post/unhas/available'
#path_topic_insp_bebe        = '/home/higo/Dev/medias_to_post/bebe/available'
#path_topic_insp_petts       = '/home/higo/Dev/medias_to_post/petts/available'


#path_dir_content = '/home/higo/Dev/default_influencer_creator/content_by_topic/'
#topic = 'unhas'

"""
pets
bebes_fofinhos
dicas_de_beleza  
make              
msgdosucesso
carros_esportivos  
insp_casamento   
make_carnaval     
quadros
cilios             
insp_unhas       
motos_esportivas  
sobrancelhas
"""


                            # 1x1
                            # 1x2 '350 250' Instagram
insMate     = '550 250'     # 1x3 '550 250' Baixador de Video
txtpad      = '740 250'     # 1x4 '740 250' Editor TXT 1
                            # 1x5



def copy_link_from_txtpad(position):

    print('     Copying Content Link')

    # Click Abrir txttap
    cmd = 'adb shell input tap ' + txtpad
    os.system(cmd)
    time. sleep(1)

    # Click Abrir primeiro Arquivo
    cmd = 'adb shell input tap 500 640'
    os.system(cmd)
    time. sleep(1)

    if position == 1:

        print('Copy Link 1')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 180 200 180 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 360'
        os.system(cmd)
        time. sleep(1)

    elif position == 2:
        print('Copy Link 2')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 280 200 280 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 460'
        os.system(cmd)
        time. sleep(1)

    elif position == 3:
        print('Copy Link 3')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 380 200 380 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 250'
        os.system(cmd)
        time. sleep(1)

    elif position == 4:
        print('Copy Link 4')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 480 200 480 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 350'
        os.system(cmd)
        time. sleep(1)

    elif position == 5:
        print('Copy Link 5')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 580 200 580 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 450'
        os.system(cmd)
        time. sleep(1)

    elif position == 6:
        print('Copy Link 6')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 680 200 680 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 550'
        os.system(cmd)
        time. sleep(1)

    elif position == 7:
        print('Copy Link 7')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 780 200 780 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 650'
        os.system(cmd)
        time. sleep(1)

    elif position == 8:
        print('Copy Link 8')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 880 200 880 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 750'
        os.system(cmd)
        time. sleep(1)

    elif position == 9:
        print('Copy Link 9')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 980 200 980 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 850'
        os.system(cmd)
        time. sleep(1)

    elif position == 10:
        print('Copy Link 10')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 1080 200 1080 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 950'
        os.system(cmd)
        time. sleep(1)

    elif position == 11:
        print('Copy Link 11')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 1180 200 1180 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 1050'
        os.system(cmd)
        time. sleep(1)

    elif position == 12:
        print('Copy Link 12')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 1280 200 1280 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 1150'
        os.system(cmd)
        time. sleep(1)

    elif position == 13:
        print('Copy Link 13')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 1380 200 1380 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 1250'
        os.system(cmd)
        time. sleep(1)

    elif position == 14:
        print('Copy Link 14')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 1480 200 1480 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 1350'
        os.system(cmd)
        time. sleep(1)

    elif position == 15:
        print('Copy Link 15')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 1580 200 1580 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 1450'
        os.system(cmd)
        time. sleep(1)

    elif position == 16:
        print('Copy Link 16')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 1680 200 1680 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 1550'
        os.system(cmd)
        time. sleep(1)

    elif position == 17:
        print('Copy Link 17')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 1780 200 1780 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 1650'
        os.system(cmd)
        time. sleep(1)

    elif position == 18:
        print('Copy Link 18')

        # Click Long Selecionar Primeiro Link
        cmd = 'adb shell input swipe 200 1880 200 1880 600'
        os.system(cmd)
        time. sleep(1)

        # Click Copy Primeiro Link
        cmd = 'adb shell input tap 440 1750'
        os.system(cmd)
        time. sleep(1)

    # Stop TXTPAD
    cmd = 'adb shell am force-stop vladyslavpohrebniakov.txtpad'
    os.system(cmd)
    time. sleep(2)

def create_caption_file(index):

    print("     Creating Caption File")

    # Click Abrir txttap
    cmd = 'adb shell input tap ' + txtpad
    os.system(cmd)
    time. sleep(2)

    # Click botao +
    cmd = 'adb shell input tap 920 1950'
    os.system(cmd)
    time. sleep(2)

    # Click botao Escrever, Palis
    cmd = 'adb shell input tap 900 1750'
    os.system(cmd)
    time. sleep(2)

    # Click No Input Title
    cmd = 'adb shell input tap 400 400'
    os.system(cmd)
    time. sleep(1)

    # Cria Input Title
    #title_file_video = str(index) + '_' + 'caption_video'
    cmd = 'adb shell input text caption_video'
    os.system(cmd)
    time. sleep(1)

    # Click Longo para aparecer opcao colar
    cmd = 'adb shell input swipe 250 700 250 700 600'
    os.system(cmd)
    time. sleep(1)

    # Clicar em Colar
    print('colar')
    cmd = 'adb shell input tap 450 550'
    os.system(cmd)
    time. sleep(10)

    # Clicar em Salvar

    print(' Click Salvar 1')
    cmd = 'adb shell input tap 950 550'
    os.system(cmd)
    time. sleep(10)
    print('CLick Salvar 2')
    cmd = 'adb shell input tap 930 280'
    os.system(cmd)
    time. sleep(10)

    # Stop TXTPAD
    cmd = 'adb shell am force-stop vladyslavpohrebniakov.txtpad'
    os.system(cmd)
    time. sleep(10)


def format_download(value, path_new_dir):

    print(' format_download() ')

    if value == 0:
        print(' Format Pure')

        print(path_new_dir)

        print(' | Criando Sub dir')
        data = datetime.now()
        sub_dir = str(data.year) + '-' + str(data.month) + '-' + str(data.day) + '_' + str(data.hour) + '-' + str(data.minute) + '-' + str(data.second)
        cmd = 'mkdir ' + path_new_dir + '/' + sub_dir
        print(cmd)
        os.system(cmd)
        time. sleep(1)

        list_files = os.listdir(path_new_dir)

        for x in list_files:

            if '.mp4' in x:

                print(' | Mover Video para Sub dir')
                cmd = 'mv ' + path_new_dir + '/' + x + ' ' + path_new_dir + '/' + sub_dir
                print(cmd)
                os.system(cmd)
                time. sleep(1)

                print(' | Criar Story')
                break_video_to_story(path_new_dir + '/' + sub_dir,x)

                print(' | Criando dir Reels')
                cmd = 'mkdir ' + path_new_dir + '/' + sub_dir + '/reel' 
                print(cmd)
                os.system(cmd)
                time. sleep(1)
                print(' | Movendo para dir Reels')
                cmd = 'mv ' + path_new_dir + '/' + sub_dir + '/' + x + ' ' + path_new_dir + '/' + sub_dir + '/reel/' + x 
                print(cmd)
                os.system(cmd)
                time. sleep(1)

            elif 'caption_' in x:

                print(' | Criando dir Caption')
                cmd = 'mkdir ' + path_new_dir + '/' + sub_dir + '/caption' 
                print(cmd)
                os.system(cmd)
                time. sleep(1)
                print(' | Movendo Caption')
                cmd = 'mv ' + path_new_dir + '/' + x + ' ' + path_new_dir + '/' + sub_dir + '/caption/'
                print(cmd)
                os.system(cmd)
                #print('\n\n\n\Ponto de Corte')
                time. sleep(2)


        print(' | Mover para z_new_medias')
        cmd = 'mv ' + path_new_dir + '/' + sub_dir + ' ' +  z_new_media
        print(cmd)
        os.system(cmd)
        time. sleep(1)




    elif value == 1:


        print(' Format Grup')
        print(path_new_dir)

        list_files = os.listdir(path_new_dir)

        for x in list_files:

            if '.mp4' in x:

                print(' | Criando Sub dir')
                data = datetime.now()
                sub_dir = str(data.year) + '-' + str(data.month) + '-' + str(data.day) + '_' + str(data.hour) + '-' + str(data.minute) + '-' + str(data.second)
                cmd = 'mkdir ' + path_new_dir + '/' + sub_dir
                print(cmd)
                os.system(cmd)
                time. sleep(1)

                print(' | Mover Video para Sub dir')
                cmd = 'mv ' + path_new_dir + '/' + x + ' ' + path_new_dir + '/' + sub_dir
                print(cmd)
                os.system(cmd)
                time. sleep(1)

                print(' | Criar Story')
                break_video_to_story(path_new_dir + '/' + sub_dir,x)

                print(' | Criando dir Reels')
                cmd = 'mkdir ' + path_new_dir + '/' + sub_dir + '/reel' 
                print(cmd)
                os.system(cmd)
                time. sleep(1)
                print(' | Movendo para dir Reels')
                cmd = 'mv ' + path_new_dir + '/' + sub_dir + '/' + x + ' ' + path_new_dir + '/' + sub_dir + '/reel/' + x 
                print(cmd)
                os.system(cmd)
                time. sleep(1)


                print(' | Criando dir Caption')
                cmd = 'mkdir ' + path_new_dir + '/' + sub_dir + '/caption' 
                print(cmd)
                os.system(cmd)
                time. sleep(1)
                print(' | Criando Caption Vazio')
                cmd = 'touch ' + path_new_dir + '/' + sub_dir + '/caption/caption_video.txt'
                print(cmd)
                os.system(cmd)
                time. sleep(1)

                print(' | Mover para z_new_medias')
                cmd = 'mv ' + path_new_dir + '/' + sub_dir + ' ' +  z_new_media
                print(cmd)
                os.system(cmd)
                time. sleep(1)




def transfer_media(index):


    # Criar DIR
    data = datetime.now()
    dir_new = str(index) + '_' + str(data.day) + '-' + str(data.month) + '-' + str(data.year) + '_' + str(data.hour) + '-' + str(data.minute) + '-' + str(data.second)

    path_dir_new = point_to_new_media + '/' + dir_new

    print(' |   ')
    print(' |   Criando Dir')
    #cmd = 'mkdir ' + dir_new
    #print(cmd)
    #os.system(cmd)
    #time. sleep(2)

    path_video = '/sdcard/Download/InsMate'
    path_file  = '/sdcard/txtpad/caption_video.txt'

    print("     Moving Files to Computer")

    # transferir video 
    cmd = 'adb pull ' + path_video + ' ' + point_to_new_media + '/' + dir_new
    print(cmd)
    os.system(cmd)
    time. sleep(3)

    # transferir file txt 
    cmd = 'adb pull ' + path_file + ' ' + point_to_new_media + '/' + dir_new
    print(cmd)
    os.system(cmd)
    time. sleep(2)

    # Apagar Video
    cmd = 'adb shell rm -r ' + path_video + '*'
    os.system(cmd)
    time. sleep(1)

    # Apagar file
    cmd = 'adb shell rm ' + path_file
    os.system(cmd)
    time. sleep(1)


    return point_to_new_media + '/' + dir_new







#def format_media():

#------

def download_reel_pure(index):

    print('     Downloading Video')

    # Click Abrir insMate - Ja baixa o Video
    cmd = 'adb shell input tap ' + insMate
    os.system(cmd)
    time. sleep(10)

    # Click Copiar Descrição
    cmd = 'adb shell input tap 815 690'
    os.system(cmd)
    time. sleep(10)

    # Recua ABA
    cmd = 'adb shell input tap 285 2200'
    os.system(cmd)
    time. sleep(10)


    # Stop VideoDownloader
    cmd = 'adb shell am force-stop videodownloader.instagram.videosaver'
    os.system(cmd)
    time. sleep(2)


    # Criar Arquivo com Descricao do video
    create_caption_file(index)

    # Passa Files para Computador
    path_new_dir = transfer_media(index)

    print(path_new_dir)

    format_download(0, path_new_dir)


def download_group(index):

    print('     DOWNLOAD GROUP')

    # Click Abrir insMate - Ja baixa o Video
    cmd = 'adb shell input tap ' + insMate
    os.system(cmd)
    time. sleep(10)

    print('')

    # Click Em Baixar Todos
    cmd = 'adb shell input tap 500 1710'
    os.system(cmd)
    time. sleep(10)



    # Click Copiar Descrição
    cmd = 'adb shell input tap 815 690'
    os.system(cmd)
    time. sleep(10)

    # Recua ABA
    cmd = 'adb shell input tap 285 2200'
    os.system(cmd)
    time. sleep(10)



    # Stop VideoDownloader
    cmd = 'adb shell am force-stop videodownloader.instagram.videosaver'
    os.system(cmd)
    time. sleep(2)



    # Criar Arquivo com Descricao do video
    create_caption_file(index)

    # Passa Files para Computador
    #transfer_media(index)

    # Passa Files para Computador
    path_new_dir = transfer_media(index)

    print(path_new_dir)

    format_download(1, path_new_dir)



def download_1_media(index, type):

    copy_link_from_txtpad(index)

    if type == 0:
        download_reel_pure(index)
    elif type == 1:
        download_group(index)

def download_all_medias_of_one_list(path_list_link):

    type_download = []

    # Le arquivo
    #----------------------------------------------
    with open(path_list_link,"r") as file1:
        file = file1.read()
    
    # Ler dados
    #-----------------------------------------------
    for x in file.split('\n'):
        
        if 'reel' in x:           
            print('->> ',x)
            type_download.append(0)
        elif 'com/p/' in x:
            print(x)
            type_download.append(1)

    print(type_download)

    path_destino = '/sdcard/txtpad'


    print(' |   Copiando Arquivo ', x ,' para Celular')
    print(' |----------------------------------------------')
    cmd = 'adb push ' + path_list_link + ' ' + path_destino
    print(cmd)
    os.system(cmd)
    print(' |----------------------------------------------')

    print('   [ download_media() ]\n')

    for x in range(18):
        #print(x+1)
        download_1_media(x+1,type_download[x])
        #copy_link_from_txtpad(x+1)


    print(' Fechou Lista')

    #print(' Vamos Formatar')
    


def download_all_list():

    path_list_links_available = '../list_links_to_download/available'
    list_list_links = os.listdir(path_list_links_available)

    for x in list_list_links:

        path_list_link = path_list_links_available + '/' + x
        print('\n')
        print(path_list_link)

        download_all_medias_of_one_list(path_list_link)

    '''
    Ler todas as Listas disponiveis
    pegar path das listas e passar uma por uma para ser baixada
    usa o for para chamar download_all_medias_of_one_list()
    '''

#------

download_all_list()

#save_media()

#download_all_medias_of_one_list()
