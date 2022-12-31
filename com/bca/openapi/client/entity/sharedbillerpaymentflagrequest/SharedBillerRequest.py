
class PaidAmount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class SharedBillerRequest():
    def jsonable(self):
        return self.__dict__

    partnerServiceId = str
    customerNo = str
    virtualAccountNo = str
    inquiryRequestId = str
    partnerReferenceNo = str
    paidAmount = PaidAmount()
    trxDateTime = str
