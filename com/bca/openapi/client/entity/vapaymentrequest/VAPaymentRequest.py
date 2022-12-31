
class FeeAmount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class FreeTexts():
    def jsonable(self):
        return self.__dict__

    english = str
    indonesia = str

class AdditionalInfo():
    def jsonable(self):
        return self.__dict__


class BillAmount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class BillDescription():
    def jsonable(self):
        return self.__dict__

    english = str
    indonesia = str

class BillDetails():
    def jsonable(self):
        return self.__dict__

    billCode = str
    billNo = str
    billName = str
    billShortName = str
    billDescription = BillDescription()
    billSubCompany = str
    billAmount = BillAmount()
    additionalInfo = AdditionalInfo()
    billReferenceNo = str

class TotalAmount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class CumulativePaymentAmount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class PaidAmount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class VAPaymentRequest():
    def jsonable(self):
        return self.__dict__
    
    partnerServiceId = str
    customerNo = str
    referenceNo = str
    virtualAccountNo = str
    virtualAccountName = str
    virtualAccountEmail = str
    virtualAccountPhone = str
    sourceAccountNo = str
    sourceAccountType = str
    inquiryRequestId = str
    partnerReferenceNo = str
    paidAmount = PaidAmount()
    cumulativePaymentAmount = CumulativePaymentAmount()
    paidBills = str
    totalAmount = TotalAmount()
    trxDateTime = str
    journalNum = str
    paymentType = str
    flagAdvise = str
    billDetails = [BillDetails()]
    freeTexts = [FreeTexts()]
    feeAmount = FeeAmount()
