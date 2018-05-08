import hashlib as hash
import json

hash_types = {
                'md5': 'md5',
                'sha1':'sha1',
                'sha224':'sha224',
                'sha256':'sha256',
                'sha384':'sha384',
                'sha512':'sha512'
            }   

def str_encode(string):
    return str(string).encode('utf-8')

def hash_functions(string, type):
    if type == 'md5':
        md5 = hash.md5(str_encode(string))
        this_digested = md5.digest()
        this_hexdigested = md5.hexdigest()
        this_copy = md5.copy()

    elif type == 'sha1':
        sha1 = hash.sha1(str_encode(string))
        this_digested = sha1.digest()
        this_hexdigested = sha1.hexdigest()
        this_copy = sha1.copy()

    elif type == 'sha224':
        sha224 = hash.sha224(str_encode(string))
        this_digested = sha224.digest()
        this_hexdigested = sha224.hexdigest()
        this_copy = sha224.copy()

    elif type == 'sha256':
        sha256 = hash.sha256(str_encode(string))
        this_digested = sha256.digest()
        this_hexdigested = sha256.hexdigest()
        this_copy = sha256.copy()

    elif type == 'sha384':
        sha384 = hash.sha384(str_encode(string))
        this_digested = sha384.digest()
        this_hexdigested = sha384.hexdigest()
        this_copy = sha384.copy()

    elif type == 'sha512':
        sha512 = hash.sha512(str_encode(string))
        this_digested = sha512.digest()
        this_hexdigested = sha512.hexdigest()
        this_copy = sha512.copy()

    else :
        print('this method ',type,' is not listed')
        return True

    hash_object =   {
                        'digested_hash': this_digested,
                        'hex_digested_hash': this_hexdigested,
                        'data':string,
                        'clone': this_copy,
                    }

    return hash_object


def show_examples(string):
    for tp in hash_types:
        print(hash_functions(string, tp))
