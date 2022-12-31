
from datetime import datetime, timedelta


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonToken(metaclass=SingletonMeta):
    token = ""
    expireTime = datetime.now()- timedelta(days=1)

    def setToken(self, tokenData, expireInSecond):
       self.token =  tokenData
       self.expireTime = datetime.now()+ timedelta(seconds=(0.8*int(expireInSecond)))

    def isExpire(self):
        currentTime = datetime.now()
        if self.expireTime < currentTime:
            """print("Expire")"""
            return True
        else:
            """print("Not Expire")"""
            return False  

    def getToken(self):
        return self.token
      

       
