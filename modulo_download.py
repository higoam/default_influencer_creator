from selenium import webdriver
import os
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By

login = 'acheipromocao_manaus'
senha = 'karen123321'
url_instagram  = 'https://www.instagram.com/'
url_conversa   = 'https://www.instagram.com/direct/t/110635423668426/'

driver = webdriver.Chrome()
driver.get(url_instagram) 
time.sleep(3)

#input login
input_login = driver.find_element(By.NAME,'username')
input_login.send_keys(login)
time.sleep(2)

#input senha
input_senha = driver.find_element(By.NAME,'password')
input_senha.send_keys(senha)
time.sleep(2)

#click button submit
click_button_Login = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
click_button_Login.click()
time.sleep(10)

#click Save Info
#click_button_Login = driver.find_element(By.CLASS_NAME,' _acan _acap _acas _aj1- _ap30')
#                                                    //*[@id="mount_0_0_dR"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button
#click_button_Login.click()
#time.sleep(3)
#<button class=" _acan _acap _acas _aj1- _ap30" type="button">Save info</button>
#<button class=" _acan _acap _acas _aj1- _ap30" type="button">Save info</button>



# Open new aba com conversa
driver.execute_script("window.open('');")
time.sleep(5)

# Troca para nova janela e abre a URL
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
driver.get('https://www.instagram.com/p/C1aCuJJp-YQ/')
time.sleep(3)

code_html = driver.page_source

mount_code = code_html.find('id="mount')

print('Idex: ', mount_code)
start_cut = mount_code
end_cut = mount_code + 10
cuted = mount_code[start_cut:end_cut]

print('string: ', cuted)

#print(code_html)
time.sleep(2)


#https://www.instagram.com/p/C1aCuJJp-YQ/


print('VAI SALVAR')

with open("/home/higo/Dev/krossy/mundodospequeninos/code/code_html.html","w") as arquivo:
    arquivo.write(code_html)
print('SALVOU')




#Procurar por mount_ dentro dessa tag
#<div id="mount_0_0_fM"><div class="">
#para achar esses dives aqui embaixo

#//*[@id="mount_0_0_GO"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div/div[17]/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/img


#click alguma media
#click_button_Login = driver.find_element(By.XPATH,'//*[@id="mount_0_0_cW"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div/div[8]/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/img')
#click_button_Login.click()
#time.sleep(5)



#//*[@id="mount_0_0_GO"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div/div[17]/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/img

#Video Aberto
#https://www.instagram.com/p/CbioMdbtLFp/

while(1):
    time.sleep(5)



'''
browser.find_element_by_name("session_key").send_keys("acheipromocao_manaus")
time.sleep(5)
browser.find_element_by_name("session_password").send_keys("SUA SENHA")
time.sleep(5)
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
time.sleep(5)
'''
#browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').click()




#login = browser.find_elements_by_xpath('//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]') 
#login[0].click() 
  
#print("Login in Twitter") 

'''  
user = browser.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input') 
user[0].send_keys('USER-NAME') 
  
user = browser.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input') 
with open('test.txt', 'r') as myfile:   
    Password = myfile.read().replace('\n', '') 
user.send_keys(Password) 
  
LOG = browser.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/input[1]') 
LOG[0].click() 
print("Login Successful") 
time.sleep(5) 
  
elem = browser.find_element_by_name("q") 
elem.click() 
elem.clear() 
  
elem.send_keys("Geeks for geeks ") 
elem.send_keys(Keys.RETURN) 

'''  
