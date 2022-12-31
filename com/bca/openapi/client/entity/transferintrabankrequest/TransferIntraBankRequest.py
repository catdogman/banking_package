
class AdditionalInfo():
    def jsonable(self):
        return self.__dict__

    beneficiaryEmail = str
    economicActivity = str
    transactionPurpose = str

class Amount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class TransferIntraBankRequest():
    def jsonable(self):
        return self.__dict__

    partnerReferenceNo = str
    amount = Amount()
    beneficiaryAccountNo = str
    currency = str
    customerReference = str
    feeType = str
    remark = str
    sourceAccountNo = str
    transactionDate = str
    additionalInfo = AdditionalInfo()
