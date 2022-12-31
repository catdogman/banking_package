
class AccountStatementRequest():
    def jsonable(self):
        return self.__dict__

    partnerReferenceNo = str
    accountNo = str
    fromDateTime = str
    toDateTime = str
