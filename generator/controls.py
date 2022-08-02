#########################################################
from .config import read_ini


def read_line():
    obj = read_ini(filename="./generator/ini.ini", selection="Address")
    return obj


###########################################################
from cryptography.fernet import Fernet


def get_key(string="none"):
    return str(Fernet.generate_key(), "utf-8")


######################################################
from hashlib import *

# md5, sha1, sha224, sha256, sha384, and sha512
import base64


def Enc(string="none"):
    encodedString = string.encode("utf8")
    # print(encodedString)
    encodedString = base64.b64encode(encodedString)
    # print(encodedString)
    sha_key = md5()
    sha_key.update(encodedString)
    data = sha_key.hexdigest()
    return data


def validate(key_received="none", string="none") -> bool:
    encodedString = string.encode("utf8")
    # print(encodedString)
    encodedString = base64.b64encode(encodedString)
    # print(encodedString)
    sha_key = md5()
    sha_key.update(encodedString)
    key = sha_key.hexdigest()
    if key == key_received:
        return True
    return False
