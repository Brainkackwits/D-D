import os
import hashlib
from main.statics import path
class register():
    def __init__(self, name , password):
        self.name = name
        self.password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),os.urandom(32),100000)
    def add(self):
        f = open(path+"demofile2.txt", "w")
        #f.write("Now the file has more content!")
        #f.close()
    def testing(self):
        pass
class user()
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def login(self):
        pass
