from EnterDetailsHere import *
# This class just freeze the child class
# So that no extra variable can be created accidentally 
class FrozenClass(object):
    __isfrozen = False
    def __setattr__(self, key, value):
        if self.__isfrozen and not hasattr(self, key):
            raise TypeError( "%r is a frozen class" % self )
        object.__setattr__(self, key, value)

    def _freeze(self):
        self.__isfrozen = True


class UserDetails(FrozenClass):

    def __init__(self):
        self.__username = username
        self.__password = password      
        self.__exceptions = self.acceptException()
        self._freeze()

    def acceptException(self) :
        exceptions_list = exceptions
        if len(exceptions_list) > 0:
            return list(map(str, exceptions_list.strip().split(" ")))
        else: 
            return []

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def getException(self):
        return self.__exceptions

    def setUsername(self,username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def __str__(self):
        return "Username: {} , Password : {} ".format(self.__username, self.__password)

if __name__ == "__main__":
    user = UserDetails()
    print(user)