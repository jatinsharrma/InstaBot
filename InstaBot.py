from Login import Login
from Profile import Profile
from UserDetails import UserDetails
from SelenumDetails import SeleniumDetails

def instBot():
    work_done = False
    while not work_done:
        user = UserDetails()
        selenium = SeleniumDetails()
        selenium.getDriver().get("https://www.instagram.com")
        login = Login(user, selenium)    
        if login.main():
            profile = Profile(user,selenium)
            if profile.main():
                work_done = True
        selenium.getDriver().quit()


if __name__ == "__main__":
    instBot()
    
     