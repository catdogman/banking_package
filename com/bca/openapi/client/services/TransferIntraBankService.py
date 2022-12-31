from com.bca.openapi.client.service.BaseService import BaseService
from com.bca.openapi.client.entity.transferintrabankresponse.TransferIntraBankResponse import TransferIntraBankResponse

import datetime
import json

def ComplexHandler(Obj):
    if hasattr(Obj, 'jsonable'):
        return Obj.jsonable()

class TransferIntraBankService(BaseService):

    def processTransferIntraBank(self, 
            external_id, 
            request):

        self.statement_path = '/openapi/v1.0/transfer-intrabank'        
        relative_url = self.statement_path
        url = self.host + relative_url
        token = self._getToken()

        timestamp = datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat()
        timestamp = timestamp[:19] + timestamp[26:]
        data = json.dumps(request,default=ComplexHandler, separators=(',', ':')).encode()
        signature = self._generate_signature("POST",relative_url,token, timestamp, data)

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'CHANNEL-ID': '95051',
            'Authorization': 'Bearer {}'.format(token),
            'Origin': self.origin,
            'X-CLIENT-KEY': self.client_id,
            'X-TIMESTAMP': timestamp,
            'X-PARTNER-ID': self.corp_id,
            'X-EXTERNAL-ID': external_id,
            'X-SIGNATURE': signature
        }
 
        response_data = self._open_url(url, data=data, headers=headers)
        response = TransferIntraBankResponse(response_data)
        return response
