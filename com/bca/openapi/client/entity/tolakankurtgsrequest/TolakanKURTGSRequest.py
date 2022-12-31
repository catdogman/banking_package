
class AdditionalInfo():
    def jsonable(self):
        return self.__dict__

    RejectStatusID = str
    RejectStatusEN = str
    traceNo = str

class Amount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class TolakanKURTGSRequest():
    def jsonable(self):
        return self.__dict__

    originalPartnerReferenceNo = str
    originalReferenceNo = str
    originalExternalId = str
    latestTransactionStatus = str
    amount = Amount()
    beneficiaryAccountName = str
    beneficiaryAccountNo = str
    beneficiaryBankCode = str
    sourceAccountNo = str
    transactionDate = str
    additionalInfo = AdditionalInfo()
