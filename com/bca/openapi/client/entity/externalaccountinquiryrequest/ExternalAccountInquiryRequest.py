
class ExternalAccountInquiryRequest():
    def jsonable(self):
        return self.__dict__

    beneficiaryBankCode = str
    beneficiaryAccountNo = str
    partnerReferenceNo = str
