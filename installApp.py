import os
import subprocess
import asyncio
import pyautogui
import fdb
import re
from time import sleep
from subprocess import PIPE, Popen
from PyQt5.QtCore    import QProcess


f = None
p = None
index = None
nameApp = None

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

def formInstall(nameApp, form):
    pass




def Install(index, form):
    global f
    global p
    global ind
    global nameApp
    f = form
    ind = index
    print(type(index))
    nameApp = checkDB(index,form)
    formInstall(nameApp,form)
    form.textInstallorDeleteLabel.setText("Устанавливаем "+nameApp)
    form.progressTextLabel.setText("Ожидайте...")
    form.installationFooter.show()

    p = QProcess()
    p.setProgram("sudo")
    p.setArguments(["dnf", "install", "-y", nameApp])
    p.finished.connect(afterInstall)
    p.start()


def afterInstall(exitCode, exitStatus):
    if exitCode == 0:
        print("Установка завершена!")
        #p = QProcess()
        os.system(nameApp)
     #   p.setProgram("")
    #    p.setArguments([nameApp])
        addLocal(ind,nameApp)
        f.installButtonPageIApp_Label.hide()
        f.deleteButtonPageIApp_Label.show()
        f.installationFooter.hide()  

    elif exitCode == 1:
        print("Ошибка при установке!")
        f.textInstallorDeleteLabel.setText("Ошибка установки "+nameApp)
        f.progressTextLabel.setText("Произошла ошибка при установке #1. Обратитесь к разработчику.")
    else:
        print("Неизвестная ошибка!")
        f.textInstallorDeleteLabel.setText("Неизвестная ошибка установки")
        f.progressTextLabel.setText("Кажется у нас интернет пропал")
    



def Remove(index, form):
    global f
    global p
    global ind
    global nameApp
    f = form
    ind = index
    print(type(index))
    nameApp = checkDB(index,form)
    formInstall(nameApp,form)
    form.textInstallorDeleteLabel.setText("Удаляем "+nameApp)
    form.progressTextLabel.setText("Ожидайте...")
    form.installationFooter.show()

    p = QProcess()
    p.setProgram("sudo")
    p.setArguments(["dnf", "remove", "-y", nameApp])
    p.finished.connect(afterRemove)
    p.start()


def afterRemove(exitCode, exitStatus):
    if exitCode == 0:
        print("Удаление завершено!")
        os.system(nameApp)
        removeLocal(ind,nameApp)
        f.installButtonPageIApp_Label.show()
        f.deleteButtonPageIApp_Label.hide()
        f.installationFooter.hide()  

    elif exitCode == 1:
        print("Ошибка при установке!")
        f.textInstallorDeleteLabel.setText("Ошибка при удалении  "+nameApp)
        f.progressTextLabel.setText("Произошла ошибка при удалении #1. Обратитесь к разработчику.")
    else:
        print("Неизвестная ошибка!")
        f.textInstallorDeleteLabel.setText("Неизвестная ошибка при удаления")
        f.progressTextLabel.setText("Мы не смогли удалить приложение, обратитесь к разработчику.")


# def Remove(index, form):
#     print(type(index))
#     nameApp = checkDB(index,form)
#     checkInstall = os.WEXITSTATUS(os.system("sudo dnf remove -y "+nameApp))
#     if checkInstall == 0:
#         print("Удаление завершено!")
#         removeLocal(index,nameApp)
#         form.deleteButtonPageIApp_Label.hide() 
#         form.installButtonPageIApp_Label.show()
        
#     elif checkInstall == 1:
#         print("Ошибка при удалении!")
#     else:
#         print("Неизвестная ошибка!")
#     #self.ui.textInstallorDeleteLabel.setText("Установка ")

def checkInstall(index,form):
    print(type(index))
    nameApp = checkDB(index,form)
    result = subprocess.check_output("sudo dnf list installed", shell=True, text=True)
    if result.find(nameApp) == -1:
        print("Отсутствует в установленных...")
        removeLocal(index,nameApp)
        return False
    else:
        print("мы нашли его!")
        return True

def checkUpdate(index,form):
    print(type(index))
    nameApp = checkDB(index,form)
    checkInstall = os.WEXITSTATUS(os.system("sudo dnf check-update "+nameApp))
    print(str(checkInstall))
    if checkInstall == 0:
        print("Присутствует")
        return True
    else:
        print("мы нашли его!")
        return False
    # checkInstall = os.WEXITSTATUS(os.system("sudo dnf list installed"))
    # print(checkInstall, " ЭТООО")
    #print("Что нам вернуло:\n", result)

# if __name__ == "__main__":
#    checkInstall("dfgfg")