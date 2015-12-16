__author__ = 'Filip'
import hashlib

key = 'bgvyzdsv'

for i in range(1,100000000):
    hash = hashlib.md5(key + str(i))
    if hash.hexdigest()[0:6] == '000000':
        print i
