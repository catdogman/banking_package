
class AdditionalInfo():
    def jsonable(self):
        return self.__dict__

    terminalId = str
    partnerMerchantType = str

class InquiryQRISRequest():
    def jsonable(self):
        return self.__dict__

    originalPartnerReferenceNo = str
    originalReferenceNo = str
    serviceCode = str
    merchantId = str
    subMerchantId = str
    additionalInfo = AdditionalInfo()
