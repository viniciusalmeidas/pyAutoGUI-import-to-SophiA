import pyautogui as pg
import os
import subprocess
from time import sleep
import pyperclip
import asyncio

def openSophia(path, login, senha):
    try:
        subprocess.Popen(path, stdout=subprocess.PIPE)# sophia = subprocess.call(path)
        sleep(1.5)
        pg.click(x=665, y=514)
        pg.write(login)
        sleep(0.5)
        pg.press('tab')
        sleep(0.5)
        pg.write(senha)
        pg.click(x=1168, y=670)
        sleep(1)
        return True
    except Exception:
        print(f'Não achamos o programa no endereço: {path}.') 
        pg.alert(f'Não achamos o programa no endereço: {path}.')
        return False
        exit()


def copiar_texto_coordenadas(a,b):
    sleep(0.75)
    pg.doubleClick(x = a, y = b)
    pg.hotkey('ctrl', 'c')
    sleep(0.5) 
    return pyperclip.paste()
     

def update_email(nome,email):
    pg.click(pg.locateCenterOnScreen('.\images\colaboradores.png'))
    sleep(0.75)  
    pg.click(x=715, y=436)
    # pg.press('f3')
    pg.write(nome)
    sleep(0.75)
    pg.press('enter')
    sleep(0.4)
    pg.press('tab')
    sleep(0.4)
    pg.press('enter')
    sleep(0.75)
    # matriculaScreen = copiar_texto_coordenadas(1575, 217)#copia texto da Screen
    # print(matriculaScreen)
    # print(matricula)
    if (1 == 1): #str(matricula)):
        pg.click(pg.locateCenterOnScreen('.\images\colaboradores.png'))
        sleep(0.5)  
        pg.doubleClick(x=509, y=676)
        # pg.keyDown('ctrl')
        # sleep(0.4)
        # pg.keyDown('shift')
        # sleep(0.4)
        # pg.press('left')
        # sleep(0.4)
        # pg.keyUp('ctrl')
        # sleep(0.4)
        # pg.keyUp('shift')
        # sleep(0.4)
        pg.write(email)
        sleep(1)
        pg.click(pg.locateCenterOnScreen('.\images\gravar.png'))
        sleep(2)
        pg.click(pg.locateCenterOnScreen('.\images\jechar.png'))
        sleep(0.5)
    else:
        pg.alert("A matricula não é igual")
        # falhaEmail.append(matricula)
        exit()
    
    

def main():
    # Login on SophiA
    login = pg.prompt(title='Import-SophiA by git:viniciusalmeidas',text= 'Qual é seu login?')
    senha = pg.password(title='Import-SophiA by git:viniciusalmeidas',text= 'Senha do SophiA?',mask='*')

    # Open program on string path
    auth = openSophia('C:\SophiA\SophiA.exe', login, senha)
    errorLogin = pg.locateCenterOnScreen('.\images\errorLogin.png')

    if (errorLogin == None) and (auth == True):
        falhaEmail = []
        
        # Update client email: Marcelo Rodrigues Costa
        update_email('Marcelo Rodrigues Costa','marcelo.costa@colegioapogeu.com.br')
        update_email('Vinicius Almeida de Souza','vinicius.souza@colegioapogeu.com.br')
    
        pg.alert('PROCESSO CONCLUIDO COM SUCESSO')
        
    else:
        print("USER INVALIDO")
        exit()





if __name__ == '__main__':
    main()











