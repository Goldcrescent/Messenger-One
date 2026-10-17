import base64
from cryptography.fernet import Fernet
from urllib.parse import parse_qs, urlparse

recieved_url = input("Enter the received URL: ")
key = input("Enter secret key: ")

parsed = urlparse(recieved_url)
fragment_params = parse_qs(parsed.fragment)
tkn_encoded = fragment_params.get('msg', [None])[0]

secret_key = base64.urlsafe_b64decode(tkn_encoded).decode('utf-8')

if tkn_encoded:
    encrypted_bytes = base64.urlsafe_b64decode(tkn_encoded.encode('utf-8'))
    cipher = Fernet(key)
    decrypted_msg = cipher.decrypt(encrypted_bytes).decode('utf-8')
    print(f"Decrypted message: {decrypted_msg}")
    
    for i in range(len(secret_key)):
        secret_key[i] = 0

del secret_key