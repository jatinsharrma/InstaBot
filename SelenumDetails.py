try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains 
except:
    print("Please install Seleniu and try again !!")
    print("Try : 'pip install selenium'")

from UserDetails import FrozenClass
import sys
from os import path
from EnterDetailsHere import *

class SeleniumDetails(FrozenClass):
    
    def __init__(self):
        self.__clock = delay
        self.__driver_path = self.driverPath()
        self.__driver = self.testingAndSettingDriver()
        

    def getDriverPath(self):
        return self.__driver_path

    def getClock(self):
        return self.__clock

    def getDriver(self):
        return self.__driver

    def setDriverPath(self,driver_path):
        self.__driver_path = driver_path

    def setClock(self, clock):
        self.__clock = clock

    def driverPath(self):
        os = sys.platform
        if os == 'linux' and path.exists("chromedriver"):
            return "./chromedriver"
        else:
            return driver_path

    def testingAndSettingDriver(self):
        try:
            driver = webdriver.Chrome(executable_path = self.__driver_path)            
            return driver
        except:
            print("Driver Path is not correct")
            exit()
    
if __name__ == "__main__":
    selenium = SeleniumDetails()