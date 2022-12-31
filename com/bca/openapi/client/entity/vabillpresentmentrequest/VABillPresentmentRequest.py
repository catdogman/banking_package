
class Amount():
    def jsonable(self):
        return self.__dict__

    value = str
    currency = str

class VABillPresentmentRequest():
    def jsonable(self):
        return self.__dict__

    partnerServiceId = str
    customerNo = str
    virtualAccountNo = str
    trxDateTime = str
    channelCode = str
    language = str
    amount = Amount()
    sourceAccountNo = str
    sourceAccountType = str
