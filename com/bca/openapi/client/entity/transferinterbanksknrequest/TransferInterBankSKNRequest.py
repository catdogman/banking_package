
class Amount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class TransferInterBankSKNRequest():
    def jsonable(self):
        return self.__dict__

    partnerReferenceNo = str
    amount = Amount()
    beneficiaryAccountName = str
    beneficiaryAccountNo = str
    beneficiaryAddress = str
    beneficiaryBankCode = str
    beneficiaryBankName = str
    beneficiaryCustomerResidence = str
    beneficiaryCustomerType = str
    beneficiaryEmail = str
    currency = str
    customerReference = str
    feeType = str
    kodepos = str
    receiverPhone = str
    remark = str
    senderCustomerResidence = str
    senderCustomerType = str
    senderPhone = str
    sourceAccountNo = str
    transactionDate = str
