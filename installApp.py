import os
import subprocess
import pyautogui
from time import sleep
from subprocess import PIPE, Popen

#a = "vlc.x86_64"
#nameApp - название устанавлимого приложения

def Install(nameApp, self, row, col, button):
    os.system("sudo dnf install -y " + nameApp)
    self.ui.textInstallorDeleteLabel.setText("Установка ")


#if __name__ == "__main__":
 #   Install()