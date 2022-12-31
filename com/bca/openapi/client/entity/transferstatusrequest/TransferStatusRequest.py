
class Amount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class TransferStatusRequest():
    def jsonable(self):
        return self.__dict__

    originalPartnerReferenceNo = str
    originalReferenceNo = str
    originalExternalId = str
    serviceCode = str
    transactionDate = str
    amount = Amount()
