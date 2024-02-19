from selenium import webdriver
import os
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By



txtpad      = '740 250'     # 1x4 '740 250' Editor TXT 1
shopee      = '140 860'

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

        # Click em Abrir
        cmd = 'adb shell input tap 200 300'
        os.system(cmd)
        time. sleep(7)



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

    # Stop TXTPAD
    cmd = 'adb shell am force-stop vladyslavpohrebniakov.txtpad'
    os.system(cmd)
    time. sleep(2)

def get_inform_of_html_page():

    print('Obter HTML da pagina para PC')

    print('Obter Sequencia de media')

    print('Obter Link do Video')




def obter_dados_app_shopee():

    # Click Abrir Carrosel
    cmd = 'adb shell input tap 550 550'
    os.system(cmd)
    time. sleep(3)

    # Click Abrir Carrosel
    cmd = 'adb shell input swipe 1000 800 200 800'
    os.system(cmd)
    time. sleep(3)

    # Click Abrir Carrosel
    cmd = 'adb shell input swipe 1000 800 200 800'
    os.system(cmd)
    time. sleep(3)

    #cria Imagem
    adb shell screencap -p /sdcard/screen.png

    Copia Imagem
    adb pull /sdcard/screen.png


    # Click Abrir Carrosel
    cmd = 'adb shell input swipe 1000 800 200 800'
    os.system(cmd)
    time. sleep(3)

    # Click Abrir Carrosel
    cmd = 'adb shell input swipe 1000 800 200 800'
    os.system(cmd)
    time. sleep(3)

    # Click Abrir Carrosel
    cmd = 'adb shell input swipe 1000 800 200 800'
    os.system(cmd)
    time. sleep(3)




    #open App Shopee

    # Click Abrir shopee
    #cmd = 'adb shell input tap ' + shopee
    #os.system(cmd)
    #time. sleep(1)

    # Click Abrir primeiro Arquivo
    #cmd = 'adb shell input tap 500 640'
    #os.system(cmd)
    #time. sleep(1)



def criar_post_shopee():
    
    copy_link_from_txtpad(1)

    obter_dados_app_shopee()


criar_post_shopee()

'''
login = 'albuquerque.higo@gmail.com'
senha = '199021H!go'
url_1   = 'https://shopee.com.br/product/376022922/22092661487?utm_campaign=-&utm_content=----&utm_medium=affiliates&utm_source=an_18386200004&utm_term=aotv71rtxdcj'

driver = webdriver.Chrome()
driver.get(url_1) 
time.sleep(3)

code_html = driver.page_source

with open("demofile3.html", "w") as file:
    file.write(code_html)

time.sleep(10)

#input login//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div[1]/div[1]/input
input_login = driver.find_element(By.NAME,'loginKey')
input_login.send_keys(login)
time.sleep(2)

#input senha
input_senha = driver.find_element(By.NAME,'password')
input_senha.send_keys(senha)
time.sleep(2)

#click button submit
click_button_Login = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[2]/form/button')
click_button_Login.click()
time.sleep(10)
'''

#while(1):
#    time.sleep(2)

#code_html = driver.page_source

#mount_code = code_html.find('id="mount')

#print('Idex: ', mount_code)
#start_cut = mount_code
#end_cut = mount_code + 10
#cuted = mount_code[start_cut:end_cut]

#print('string: ', cuted)
