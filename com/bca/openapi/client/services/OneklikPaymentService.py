from com.bca.openapi.client.service.BaseService import BaseService
from com.bca.openapi.client.entity.oneklikpaymentresponse.OneklikPaymentResponse import OneklikPaymentResponse

import datetime
import json

def ComplexHandler(Obj):
    if hasattr(Obj, 'jsonable'):
        return Obj.jsonable()

class OneklikPaymentService(BaseService):

    def payment(self, 
            external_id,
            ip_address,
            device_id,            
            request):

        self.statement_path = '/openapi/oneklik/v1.0/debit/payment-host-to-host'        
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
            'CHANNEL-ID': '95221',
            'Authorization': 'Bearer {}'.format(token),
            'Origin': self.origin,
            'X-CLIENT-KEY': self.client_id,
            'X-TIMESTAMP': timestamp,
            'X-PARTNER-ID': self.corp_id,
            'X-IP-ADDRESS': ip_address,
            'X-DEVICE-ID': device_id,
            'X-EXTERNAL-ID': external_id,
            'X-IP-ADDRESS': ip_address,
            'X-DEVICE-ID': device_id,
            'X-SIGNATURE': signature
        }
 
        response_data = self._open_url(url, data=data, headers=headers)
        response = OneklikPaymentResponse(response_data)
        return response
