
class AdditionalInfo():
    def jsonable(self):
        return self.__dict__

    additionalInfo = str
    merchantLogoUrl = str

class AdditionalData():
    def jsonable(self):
        return self.__dict__

    userId = str

class OneklikAccountBindingRequest():
    def jsonable(self):
        return self.__dict__

    merchantId = str
    additionalData = AdditionalData()
    additionalInfo = AdditionalInfo()
