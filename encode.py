import base64
import urllib
from cryptography.fernet import Fernet
from urllib.parse import urlencode

key = Fernet.generate_key()
cipher = Fernet(key)

secret_msg = input("Enter your message: ")
url = 'https://www.secret.goldcrestpvp.tech/secret'

encrypted_bytes = cipher.encrypt(secret_msg.encode('utf-8'))

encoded_tkn = base64.urlsafe_b64encode(encrypted_bytes).decode('utf-8')

final_url = f"{url}#msg={encoded_tkn}"
print(f"Generated: {final_url}")
print(f"Secret key: {key.decode('utf-8')}")