
class TransAmount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class AdditionalInfo():
    def jsonable(self):
        return self.__dict__

    userId = str
    transAmount = TransAmount()
    phoneId = str

class OneklikGeneratePaymentOTPRequest():
    def jsonable(self):
        return self.__dict__

    journeyId = str
    bankCardToken = str
    merchantId = str
    partnerReferenceNo = str
    trxDateTime = str
    additionalInfo = AdditionalInfo()
