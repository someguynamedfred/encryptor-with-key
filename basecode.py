import os
import thekey
clearance = False
unencrypted = input("What do you want your password to be? ")

access_key = input("What is the access key? ")
clearance = thekey.check_access(access_key)

encrypted_phrase = thekey.encrypt_password(unencrypted)
print(encrypted_phrase)

print(thekey.unencrypt_password(clearance, encrypted_phrase))
