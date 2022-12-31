
class SettlementQRISRequest():
    def jsonable(self):
        return self.__dict__

    merchantId = str
    terminalId = str
    partnerMerchantType = str
    totalRecord = str
    totalBaseAmount = str
    totalAmount = str
    partnerSettlementNo = str
