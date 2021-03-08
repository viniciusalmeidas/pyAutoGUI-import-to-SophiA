import pyautogui as pg
import os
import subprocess
from time import sleep
import pyperclip
import asyncio
import email

def openSophia(path, login, senha):
    try:
        subprocess.Popen(path, stdout=subprocess.PIPE)# sophia = subprocess.call(path)
        sleep(5)
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
    sleep(1)  
    pg.click(x=715, y=436)
    pg.write(nome)
    sleep(0.75)
    pg.press('enter')
    sleep(8)
    pg.click(x=1084, y=330)
    sleep(1.5)
    if (1 == 1): #str(matricula)):
        pg.doubleClick(x=1145, y=378)
        pg.write(email)
        sleep(0.5)
        pg.click(pg.locateCenterOnScreen('.\images\gravar.png'))
        sleep(5)
        pg.click(pg.locateCenterOnScreen('.\images\jechar.png'))
        sleep(1)
    else:
        pg.alert("A matricula não é igual")
        # falhaEmail.append(matricula)
        exit()
    
    

def main():
    # login = pg.prompt(title='Import-SophiA by git:viniciusalmeidas',text= 'Qual é seu login?')
    # senha = pg.password(title='Import-SophiA by git:viniciusalmeidas',text= 'Senha do SophiA?',mask='*')

    # Open program on string path
    auth = openSophia('C:\SophiA\SophiA.exe', 'VINICIUSS', '123456')
    errorLogin = pg.locateCenterOnScreen('.\images\errorLogin.png')
    
    # print(email.listaEmails)
    if (errorLogin == None) and (auth == True):
        
        # Update client email
        # for nome in email.listaEmails:
        # update_email(nome, email.listaEmails[nome])
        update_email('MARCELO RODRIGUES COSTA','marcelo.costa@colegioapogeu.com.br')

        pg.alert('PROCESSO CONCLUIDO COM SUCESSO')
    else:
        print("USER INVALIDO")
        exit()



if __name__ == '__main__':
    main()




    






