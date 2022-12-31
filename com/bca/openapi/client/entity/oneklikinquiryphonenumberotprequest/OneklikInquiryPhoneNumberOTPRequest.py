
class AdditionalInfo():
    def jsonable(self):
        return self.__dict__

    userId = str
    xcoId = str

class OneklikInquiryPhoneNumberOTPRequest():
    def jsonable(self):
        return self.__dict__

    merchantId = str
    additionalInfo = AdditionalInfo()
