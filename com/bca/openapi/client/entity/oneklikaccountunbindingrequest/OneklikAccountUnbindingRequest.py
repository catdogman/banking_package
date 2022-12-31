
class AdditionalInfo():
    def jsonable(self):
        return self.__dict__

    xcoId = str

class OneklikAccountUnbindingRequest():
    def jsonable(self):
        return self.__dict__

    merchantId = str
    additionalInfo = AdditionalInfo()
