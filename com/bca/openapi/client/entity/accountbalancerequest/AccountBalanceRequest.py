
class AccountBalanceRequest():
    def jsonable(self):
        return self.__dict__

    partnerReferenceNo = str
    accountNo = str
