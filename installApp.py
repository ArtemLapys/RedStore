import os
import subprocess
import asyncio
import pyautogui
import fdb
import re
from time import sleep
from subprocess import PIPE, Popen


def checkDB(index, form):
    cur = form.con.cursor()
    cur.execute("SELECT LOWER(INSTALL_PACK) FROM App WHERE ID= " + str(index))
    return cur.fetchone()[0]

def addLocal(index, installPack):
    file = open("baseApp.dat", 'a')
    file.write(str(index) + " " + str(installPack)+"\n")
    file.close

def removeLocal(index, installPack):
    with open("baseApp.dat", 'r') as file:
        lines = file.readlines()
    search = str(index) + " " + str(installPack)
    with open("baseApp.dat", 'w') as file:
        pattern = re.compile(re.escape(search))
        for line in lines:
            result = pattern.search(line)
            print(line)
            if result is None:
                file.write(line)            

def Install(index, form):
    print(type(index))
    nameApp = checkDB(index,form)
    form.installationFooter.show()
    checkInstall = os.WEXITSTATUS(os.system("sudo dnf install -y "+nameApp))
    if checkInstall == 0:
        print("Установка завершена!")
        os.system(nameApp)
        addLocal(index,nameApp)
        form.installButtonPageIApp_Label.hide()
        form.deleteButtonPageIApp_Label.show()
        form.installationFooter.hide()  
     #   con = fdb.connect(host=hostDB, database=DB, user=userLogin, password=userPassword, charset='UTF8')

    elif checkInstall == 1:
        print("Ошибка при установке!")
    else:
        print("Неизвестная ошибка!")
    
    #self.ui.textInstallorDeleteLabel.setText("Установка ")

def Remove(index, form):
    print(type(index))
    nameApp = checkDB(index,form)
    checkInstall = os.WEXITSTATUS(os.system("sudo dnf remove -y "+nameApp))
    if checkInstall == 0:
        print("Удаление завершено!")
        removeLocal(index,nameApp)
        form.deleteButtonPageIApp_Label.hide() 
        form.installButtonPageIApp_Label.show()
        
    elif checkInstall == 1:
        print("Ошибка при удалении!")
    else:
        print("Неизвестная ошибка!")
    #self.ui.textInstallorDeleteLabel.setText("Установка ")

def checkInstall(index,form):
    print(type(index))
    nameApp = checkDB(index,form)
    result = subprocess.check_output("sudo dnf list installed", shell=True, text=True)
    if result.find(nameApp) == -1:
        print("Отсутствует в установленных...")
        return False
    else:
        print("мы нашли его!")
        return True
    # checkInstall = os.WEXITSTATUS(os.system("sudo dnf list installed"))
    # print(checkInstall, " ЭТООО")
    #print("Что нам вернуло:\n", result)

# if __name__ == "__main__":
#    checkInstall("dfgfg")