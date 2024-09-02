import base64
import hmac
import time
from hashlib import sha1
from struct import pack, unpack

def base32_decode(encoded_key):
    """
    Decode a base32 encoded key.
    :param encoded_key: The base32 encoded secret key.
    :return: The decoded byte key.
    """
    try:
        return base64.b32decode(encoded_key, True)
    except Exception as e:
        raise ValueError("Invalid base32 encoding.") from e

def generate_totp(secret):
    """
    Generate a Time-Based One-Time Password (TOTP) using the given secret.
    :param secret: A base32 encoded secret key.
    :return: The generated TOTP as a string.
    """
    key = base32_decode(secret)
    timestamp = int(time.time()) // 30
    msg = pack(">Q", timestamp)
    
    hmac_hash = hmac.new(key, msg, sha1).digest()
    offset = hmac_hash[-1] & 0x0F
    code = unpack(">I", hmac_hash[offset:offset + 4])[0] & 0x7FFFFFFF
    otp = code % 1000000
    return f"{otp:06d}"

def verify_totp(secret, otp):
    """
    Verify a Time-Based One-Time Password (TOTP) using the given secret.
    :param secret: A base32 encoded secret key.
    :param otp: The OTP to verify.
    :return: True if the OTP is valid, False otherwise.
    """
    # Check the OTP for the current and previous time intervals
    for i in range(-1, 2):
        key = base32_decode(secret)
        timestamp = (int(time.time()) // 30) + i
        msg = pack(">Q", timestamp)
        
        hmac_hash = hmac.new(key, msg, sha1).digest()
        offset = hmac_hash[-1] & 0x0F
        code = unpack(">I", hmac_hash[offset:offset + 4])[0] & 0x7FFFFFFF
        generated_otp = f"{code % 1000000:06d}"
        
        if generated_otp == otp:
            return True
    return False
