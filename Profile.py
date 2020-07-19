from time import sleep
import random

class Profile:

    def __init__(self, user_details, driver_details):
        self.username = user_details.getUsername()
        self.driver = driver_details.getDriver()
        self.clock = driver_details.getClock()
        self.followers = user_details.getException()
        self.following = []
        self.unfollowList = []

    def main(self):
        if self.openProfile() :
            if self.getFollowers() :
                if self.getFollowing() :
                    return self.unfollow()
        return False

    def openProfile(self):
        try:
            sleep(self.clock)
            self.driver.get("https://www.instagram.com/{}".format(self.username))
            sleep(self.clock)
        except:
            print("Error opening Profile")
            return False
        return True   

    def differenceFollowingFollower(self):
        difference =  list(set(self.following).difference(set(self.followers)))
        return difference

    def getFollowers(self):
        try:
            count = int(self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text)           
            while count > len(self.followers): 
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
                self.followers = self.getNames()
            print("\nUsers who are following you : \n\n{}".format(self.followers))
            print("\nFollowers + Exceptions : {}\n".format(len(self.followers)))
            print('--------------------------------------------------------------------')
        except:
            print("Error getting followers list")
            return False
        return True

    def getFollowing(self):
        try:
            count = int(self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text)   
            while count+1 != len(self.following):
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()  
                self.following = self.getNames()
                #print(self.following)
                print(len(self.following))
            print("\nUsers whom you are following : \n\n{}".format(self.following))
            print("\nFollowing : {}\n".format(len(self.following)))
            print('--------------------------------------------------------------------')
        except:
            print("Error getting followers list")
            return False
        return True

    def getNames(self):
        scroll_box = self.scroll()
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names

    def scroll(self):
        sleep(self.clock)
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)        
        return scroll_box

    def unfollow(self):
        self.unfollowList = self.differenceFollowingFollower()
        print("\nUsers we are unfollowing : \n\n{}".format(self.unfollowList))
        print("\nNumber of accounts we are unfollowing : {}\n".format(len(self.unfollowList)))
        print('--------------------------------------------------------------------')

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        scroll_box = self.scroll()
        buttons = scroll_box.find_elements_by_xpath("//button[@class='sqdOP  L3NKy    _8A5w5    ']")
        i = 0
        rand_m = 5

        for user in self.unfollowList:
            print(str(user))
            sleep(0.5)
            try:
                self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button[2]').click()
                print('Click on "Report Problem" button and close the program by clicking Ctrrl + C \nand try again tomorrow or this will take alot time')
                return False
            except:
                buttons[self.following.index(str(user))].click()
                self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
                sleep(random.randint(20,40))
                if i == rand_m :
                    rand_m = random.randint(4,7)
                    sleep(random.randint(random.randint(50,80),random.randint(80,100)))
                    i = 0
                i += 1
        return True


#------------------------------
#---------Extra----------------
#------------------------------

        # n = 0
        # while n < (count//5):
        #     n += 1
        #     self.driver.execute_script("""
        #         arguments[0].scrollTo(0, arguments[0].scrollHeight); 
        #         """, scroll_box)  
        #     sleep(1)     