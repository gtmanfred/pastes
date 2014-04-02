import Crypto.Random
import re

def gen_random(length=8):
    pasteid = ''
    while len(pasteid) < length:
        pasteid += re.sub(r'\W', '', Crypto.Random.get_random_bytes(1))

    return pasteid
