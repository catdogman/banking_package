
class AdditionalInfo():
    def jsonable(self):
        return self.__dict__

    convenienceFee = str
    partnerMerchantType = str
    terminalLocationName = str

class FeeAmount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class Amount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class OpenAPI-QRIS-GenerateRequest():
    def jsonable(self):
        return self.__dict__

    partnerReferenceNo = str
    amount = Amount()
    feeAmount = FeeAmount()
    merchantId = str
    subMerchantId = str
    terminalId = str
    additionalInfo = AdditionalInfo()
