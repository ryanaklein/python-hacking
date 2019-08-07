from datetime import datetime
from datetime import timedelta
import json

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

from jose.backends import RSAKey
from jose.constants import ALGORITHMS
from jose import jws,jwt

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)


pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption())

pem = str(pem,'utf-8')




public_key = private_key.public_key()

rsakey = RSAKey(public_key, ALGORITHMS.RS256)

print(rsakey.to_dict())

tomorrow = datetime.now() + timedelta(days=1)
tomorrow_in_seconds = tomorrow.timestamp()



payload = {
  "sub": "a3bc91e1-dd79-433c-a3be-d5fe5ad5c608",
  "email_verified": False,
  "iss": "https://cognito-idp.us-east-2.amazonaws.com/us-east-2_rBDyyW1zu",
  "cognito:username": "a3bc91e1-dd79-433c-a3be-d5fe5ad5c608",
  "custom:Role": "Administrator",
  "aud": "f2alqmli8o74m8f63eb9qkdmm",
  "event_id": "51a8f501-b992-46ec-afd2-9eabf9ee36ff",
  "token_use": "id",
  "auth_time": 1564173531,
  "custom:Client": "High Peaks Solutions",
  "exp": round(tomorrow_in_seconds),
  "iat": 1564516708,
  "email": "Robert.Rice@highpeakssolutions.com"
}


token = jwt.encode(payload, pem, algorithm=ALGORITHMS.RS256, headers={"kid":"1", "alg":"RS256"})

print(token)










