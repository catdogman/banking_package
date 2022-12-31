
class BillDetails():
    def jsonable(self):
        return self.__dict__

    subCompanyCode = str
    subBillAmount = str

class AdditionalInfo():
    def jsonable(self):
        return self.__dict__

    userId = str
    customerName = str
    description = str
    paymentType = str
    transactionTime = str
    xcoId = str
    billDetails = [BillDetails()]

class FeeAmount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class TransAmount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class PayOptionDetails():
    def jsonable(self):
        return self.__dict__

    payMethod = str
    payOption = str
    transAmount = TransAmount()
    feeAmount = FeeAmount()

class OneklikPaymentRequest():
    def jsonable(self):
        return self.__dict__

    partnerReferenceNo = str
    merchantId = str
    payOptionDetails = [PayOptionDetails()]
    additionalInfo = AdditionalInfo()
