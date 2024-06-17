"""
      In this file will be some utility functions
"""

import hashlib

def hash_password(password) -> str:
   password_bytes = password.encode('utf-8')
   hash_object = hashlib.sha256(password_bytes)
   return hash_object.hexdigest()
