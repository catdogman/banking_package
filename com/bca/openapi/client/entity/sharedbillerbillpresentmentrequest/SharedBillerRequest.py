
class SharedBillerRequest():
    def jsonable(self):
        return self.__dict__

    partnerServiceId = str
    customerNo = str
    partnerReferenceNo = str
    virtualAccountNo = str
    trxDateTime = str
