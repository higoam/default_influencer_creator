import os
import time
from datetime import datetime, timedelta
from processamento_video import ProcessamentoVideo

class Publish_on_tap(object):

    def publish_story(self, full_path_file, name_file):

        processaVideo = ProcessamentoVideo()

        size_video = processaVideo.get_durantion_video(full_path_file)

        result_div = int(size_video/60)

        if result_div == 0:
            print('Menos de 1min')
            print('Chapa Metodo Publicar no Story')
            

        elif result_div == 1:
            print('A partir de 1min, menor que 2 min')
            
            # Quebrar 2 partes

        elif result_div == 2:            
            print('A partir de 2min, menor que 3 min')
            # Quebrar 3 partes


        elif result_div == 3:            
            print('A partir de 3min, menor que 4 min')
            # Quebrar 4 partes

        else:
            print('Nao Publica, maior que 4 minutos')
            #Nao publica


        print('   >>','Tamanho do Video:',size_video)


        print('   [ Falta Implementar: Publica no Story ]\n')


    def publish_reels(self, full_path_file, name_file):

        print(' |   Publica no Reels')    

        #print('   [ Falta Implementar: verificar se celular ta conecatado ]\n')

        path_origem = full_path_file
        path_destino = '/sdcard/Download'

        # Copiar Video para Celular
        print(' |   Copiando Arquivos para Celular\n')
        cmd = 'adb push ' + path_origem + ' ' + path_destino
        print(cmd)
        os.system(cmd)


        # Entrar em File App
        print('\n |   Disponibilizar Video')
        cmd = 'adb shell input tap 175 250'
        os.system(cmd)
        time. sleep(2)

        # Entrar no Dir Download, Preciso disso pra enchergar o novo video
        cmd = 'adb shell input tap 300 1300'
        os.system(cmd)
        time. sleep(2)


        # Open botao home, verifica nome
        cmd = 'adb shell input tap 850 2200'
        os.system(cmd)
        time. sleep(2)
        # Fechar File App
        cmd = 'adb shell input swipe 500 1200 500 700'
        os.system(cmd)
        time. sleep(2)


        # Abrir Instagram App
        cmd = 'adb shell input tap 350 250'
        os.system(cmd)
        time. sleep(2)

        # TIME to UPDATE
        time. sleep(8)

        # Click - Botao Add Puplicacao +
        cmd = 'adb shell input tap 500 2000'
        os.system(cmd)
        time. sleep(10)

        # Click - Escolher RELL
        print(' |   Escolher REELs')                
        cmd = 'adb shell input tap 950 1950'
        os.system(cmd)
        time. sleep(2)

        # Click - Aba com opcaoes de dir
        cmd = 'adb shell input tap 230 700'
        os.system(cmd)
        time. sleep(2)

        # Click - Escolher Grade de Recentes
        cmd = 'adb shell input tap 200 1000'
        os.system(cmd)
        time. sleep(2)

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
        #time.sleep(2)
        #cmd = 'adb shell input tap 200 350'
        #os.system(cmd)
        #time.sleep(2)    
        #cmd = 'adb shell input text \'\#vibebelezamanaus%s\#manaus \''
        #os.system(cmd)
        #time.sleep(2)

        # Recua teclado 1
        #time.sleep(2)
        #cmd = 'adb shell input tap 300 2200'
        #os.system(cmd)
        #time.sleep(2)

        # Recua teclado 2

        # Add Topics

        # Add Location

        # Click Compartilhar
        time.sleep(2)
        cmd = 'adb shell input tap 800 2000'
        os.system(cmd)

        # TIME to UPLOAD
        print(' |   Iniciando Upload Video')
        time. sleep(30)
        print(' |   Uploading Video')
        time. sleep(30)

        print(' |   Fechar Instagram')
        # Open botao home, verifica nome
        cmd = 'adb shell input tap 850 2200'
        time. sleep(2)
        os.system(cmd)

        # Fechar File App
        cmd = 'adb shell input swipe 500 1200 500 700'
        time. sleep(2)
        os.system(cmd)

        # Apagar os Arquivos de Dentro do Celular
        #print('\n   [ Falta Implementar: Apagar os Arquivos de Dentro do Celular ]\n')
        #cmd = 'adb shell \"rm /sdcard/Download/' + name_file + '\"'
        #time. sleep(2)
        #print(cmd)
        #os.system(cmd)



        # Open botao Recentes
        #cmd = 'adb shell input tap 850 2200'
        #os.system(cmd)
        #time. sleep(2)
        # Fechar Instagram
        #cmd = 'adb shell input swipe 500 1200 500 700'
        #os.system(cmd)
        #time. sleep(2)

        # Stop Instagram
        #cmd = 'adb shell pm clear com.instagram.android'
        #os.system(cmd)
        #time. sleep(2)


        #/sdcard/Download/studiodudapinheiro__3234034074644464727.mp4