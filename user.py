import os
import hashlib, binascii, os
from main import statics
def hash_password(password):
    salt = hashlib.sha256(os.urandom(10)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password
class register():
    def __init__(self, name , password):
        self.name = name
        self.password = password
    def add(self):
        udaten = open(statics.path+"\\load\\user.daten", 'a')
        udaten.write(str(self.name)+" "+str(hash_password(self.password))+"\n")
        udaten.close()
    def testing(self):
        udaten = open(statics.path+"\\load\\user.daten", "r")
        for daten in udaten.read().split("\n"):

            udata = daten.split(" ")
            if udata[0] == self.name:
                if verify_password(udata[1],self.password):
                    return True


ur = register("Brainkackwits","test")

if not ur.testing():
    ur.add()
