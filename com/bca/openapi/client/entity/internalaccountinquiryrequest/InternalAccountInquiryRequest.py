
class InternalAccountInquiryRequest():
    def jsonable(self):
        return self.__dict__

    partnerReferenceNo = str
    beneficiaryAccountNo = str
