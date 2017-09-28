from sha3 import sha3_256
import time
import math

def encrypt(message,key):
    s = key+message
    s_bytes = s.encode()
    s_encrypted = sha3_256(s_bytes).hexdigest()

    return s_encrypted

def is_proper_float(s):
    try:
        a = float(s)
        if (math.isnan(a) or math.isinf(a)):
            return False
        return True
    except:
        return False

def format_token(exp_time, s_encrypted):
    return "exp={}&digest={}".format(exp_time,s_encrypted)

def generate_token(key, days=1):
    """Generate a token with an expiry date, the token is encrypted so that
    users cannot change the expiry date

    :param key: (required) secret key string, not known to users
    :days: (required) the number of days the token should be valid for

    :return: encrypted token
    """
    if type(key) != str:
        raise RuntimeError('key {} is not a string'.format(key))
    exp_time = time.time()+3600*24*days
    t = str(exp_time)

    s_encrypted = encrypt(t,key)

    token = format_token(exp_time,s_encrypted)
    return token

def token_is_valid(token, key):
    """
    Check whether the expiration date of a token has passed

    :param token: an encrypted token
    :param key: the secret key the token was encrypted with

    :return: True if token is still valid
    """
    if type(token) != str: return False

    if not ('exp=' in token and '&digest=' in token): return False

    exp_time = token.split('&')[0].replace('exp=','')

    if not is_proper_float(exp_time): return False

    if float(exp_time) < time.time():
        return False

    s_encrypted = encrypt(exp_time,key)

    n_token = format_token(exp_time,s_encrypted)

    return n_token == token
