
import base64
import datetime
import hashlib
import hmac
import json
import urllib.request
import urllib.error
from com.bca.openapi.client.utils.SignatureUtil import SignatureUtil
from com.bca.openapi.client.utils.SingletonToken import SingletonToken

class BaseService():

    def __init__(self, host,origin, corp_id, client_id, client_secret, private_key, timeout_second):
        self.host = host
        self.origin = origin
        self.corp_id = corp_id
        self.client_id =client_id
        self.client_secret = client_secret
        self.private_key = private_key
        self.timeout_second = timeout_second
        self.oauth_path = '/openapi/v1.0/access-token/b2b'
        self.is_token_cache = True

    def setCacheTokenDisable(self):
        self.is_token_cache = False
    
    def _open_url(self, url, data=None, headers=None):
        ''' Helper to call urlopen
        '''
        try:
            if data:
                request = urllib.request.Request(url, data=data, headers=headers)
            else:
                request = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(request, timeout=self.timeout_second) as response:
                response_data = json.loads(response.read().decode('UTF-8'))
                return response_data
        except urllib.error.HTTPError as err:
            error_content = json.loads(err.read().decode('UTF-8'))
            return error_content
        except urllib.error.URLError as err:
            raise err

    def _generate_signature(self, http_method, relative_url, token, iso_timestamp, request_body=b''):
        signatureUtil =  SignatureUtil()
        signature = signatureUtil.generateServiceSignature(self.client_secret, http_method, relative_url, token, iso_timestamp, request_body)
        return signature
  
    def _getToken(self):
        if (self.is_token_cache):
           singletonToken = SingletonToken()
           if singletonToken.isExpire():
               response_token = self.sign_in()
               token = response_token['accessToken']
               expire_in = response_token['expiresIn']
               singletonToken.setToken(token,expire_in)
           return singletonToken.getToken()
        else:
            response_token = self.sign_in()
            token = response_token['accessToken']
            return token

    def sign_in(self):
        timestamp = datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat()
        timestamp = timestamp[:19]+timestamp[26:]
        url = self.host + self.oauth_path
        data = b'{"grantType":"client_credentials"}'
        signatureUtil =  SignatureUtil()
        signStr  = signatureUtil.generateOauthSignature(self.private_key,self.client_id,timestamp)
        headers = {
            'Content-Type': 'application/json',
            'X-TIMESTAMP' : timestamp,
            'X-CLIENT-KEY':self.client_id,
            'X-SIGNATURE': signStr
        }
        response_data = self._open_url(url, data=data, headers=headers)
        return response_data