
class Amount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class TransferInterBankONLRequest():
    def jsonable(self):
        return self.__dict__

    partnerReferenceNo = str
    amount = Amount()
    beneficiaryAccountName = str
    beneficiaryAccountNo = str
    beneficiaryAddress = str
    beneficiaryBankCode = str
    beneficiaryBankName = str
    beneficiaryEmail = str
    currency = str
    customerReference = str
    sourceAccountNo = str
    transactionDate = str
    feeType = str
