
class VAPaymentStatusRequest():
    def jsonable(self):
        return self.__dict__

    partnerServiceId = str
    customerNo = str
    virtualAccountNo = str
    inquiryRequestId = str
    paymentRequestId = str
