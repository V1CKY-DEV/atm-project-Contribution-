import hashlib
import os 


def hash_password(password):
    salt = os.urandom(16)
    hash_obj =hashlib.pbkdf2_hmac('sha256',password.encode(),salt,100000)
    return salt + hash_obj

def check_password(hashed_password,password):
    hashed_password = bytes.fromhex(hashed_password)
    salt = hashed_password[:16]
    hash_obj = hashlib.pbkdf2_hmac('sha256',password.encode(),salt,100000)
    return hashed_password[16:] == hash_obj