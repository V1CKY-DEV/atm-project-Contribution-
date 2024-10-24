import hashlib
import os 

#Created hashers for the password cause if i hear password i see hashes and salts 


#this function takes the password as string and converts it into hash returns it
def hash_password(password):
    salt = os.urandom(16)
    hash_obj =hashlib.pbkdf2_hmac('sha256',password.encode(),salt,100000)
    return salt + hash_obj
#this function takes hashed password from storage in this case we have Accounts.txt and password(converted into hash) from login input or changepassword and returns if the stored password and the input password are equal then returns true or false
def check_password(hashed_password,password):
    hashed_password = bytes.fromhex(hashed_password)
    salt = hashed_password[:16]
    hash_obj = hashlib.pbkdf2_hmac('sha256',password.encode(),salt,100000)
    return hashed_password[16:] == hash_obj