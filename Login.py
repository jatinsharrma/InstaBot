from time import sleep
import random
from UserDetails import UserDetails
from SelenumDetails import SeleniumDetails

class Login:
    def __init__(self,user_details, driver_details):
        # for profile
        self.user_details = user_details
        self.driver_details = driver_details

        # for login to work
        self.username = user_details.getUsername()
        self.password = user_details.getPassword()
        self.clock = driver_details.getClock()
        self.driver = driver_details.getDriver()
        

    def main(self): 
        # Login
        if self.login() :
            # closing Session save popup
            if self.dontSaveLoginInfo() :
                # Turning of notification
                if self.turnOffNotification():
                    return True
        return False
                

    def click(self, arg):
        sleep(self.clock)
        self.driver.find_element_by_xpath(arg).click()
        sleep(self.clock)

    def dontSaveLoginInfo(self):
        try:
            self.click('//*[@id="react-root"]/section/main/div/div/div/div/button')
        except:
            print("No Save login Dialog box Appeared. Error !!")
            return False
        return True

    def turnOffNotification(self):
        try : 
            self.click('/html/body/div[4]/div/div/div/div[3]/button[2]')
        except:
            print("Error in turning of notification")
            return False
        return True

    def login(self):

        # Wromg/Right Username and password flag
        wrong = False

        try:
            sleep(self.clock)
            username = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
            password = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
            username.send_keys(self.username)
            password.send_keys(self.password)

            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]').click()
            
            sleep(self.clock)
            
            try:
                self.driver.find_element_by_xpath('//*[@id="slfErrorAlert"]')
                wrong = True
            except:
                print("Login Successful")

            if wrong == True:
                print("Wrong Username/Password !!")
                raise Exception

        except :
            print("Error while logging in")
            return False
        return True  


if __name__ == "__main__":
    bot = InstaBot(UserDetails,SeleniumDetails)
