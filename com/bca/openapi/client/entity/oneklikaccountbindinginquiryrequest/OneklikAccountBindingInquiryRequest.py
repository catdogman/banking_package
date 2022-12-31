
class AdditionalInfo():
    def jsonable(self):
        return self.__dict__

    userId = str
    requestIds = [str()]

class OneklikAccountBindingInquiryRequest():
    def jsonable(self):
        return self.__dict__

    additionalInfo = AdditionalInfo()
