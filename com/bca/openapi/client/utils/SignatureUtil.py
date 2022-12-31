import base64
import hashlib
import hmac

from Crypto.Signature import PKCS1_v1_5  # pip install pycryptodomex
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

class SignatureUtil:
     def generateOauthSignature(self, private_key_str, client_id, iso_time):
        private_key = RSA.importKey(base64.decodebytes(private_key_str.encode()))
        signer = PKCS1_v1_5.new(private_key)
        dataToSign = client_id+"|"+iso_time
        signature = signer.sign(SHA256.new(dataToSign.encode()))
        signStr =  base64.b64encode(signature).decode('UTF-8')
        '''signStr = signature.hex()'''
        return signStr

     def validateOauthSignature(self, public_key_str, client_id, iso_time, signature):
        public_key = RSA.importKey(base64.decodebytes(public_key_str.encode()))
        signer = PKCS1_v1_5.new(public_key)
        dataToSign = client_id+"|"+iso_time
        '''if signer.verify(SHA256.new(dataToSign.encode()),bytes.fromhex(signature)):'''
        if signer.verify(SHA256.new(dataToSign.encode()),bytes.fromhex(signature)):
            return True
        else:
            return False
         
     def generateServiceSignature(self, client_secret, http_method, relative_url, token, iso_timestamp, request_body=b''):
        signature = hmac.new(client_secret.encode(), digestmod=hashlib.sha512)
        string_to_sign = http_method + ':' + relative_url + ':' + token + ':' + hashlib.sha256(request_body).hexdigest() + ':' + iso_timestamp
        signature.update(string_to_sign.encode())
        return base64.b64encode(signature.digest()).decode('UTF-8')
        '''return signature.hexdigest()''' 

     def validateServiceSignature(self, client_secret, http_method, relative_url, token, iso_timestamp, request_body, signatureIn):
        signature = hmac.new(client_secret.encode(), digestmod=hashlib.sha512)
        string_to_sign = http_method + ':' + relative_url + ':' + token + ':' + hashlib.sha256(request_body).hexdigest() + ':' + iso_timestamp
        signature.update(string_to_sign.encode())
        signatureStr = self.generateServiceSignature(client_secret, http_method, relative_url, token, iso_timestamp, request_body)
        if signatureStr == signatureIn:
            return True
        else:
            return False
