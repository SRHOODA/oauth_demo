import random
import string
import base64
import hashlib

code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128)))

code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')

print(code_verifier)
print(code_challenge)

client_id = "ehMiCBpfvYXFa70KlDs7Nx5aZgAvEZZmQsKUCq4J"
secret = "c7F7fnFvz7Ez3oRVoth7bNznh4D5mvebWEljGLM0vcTrbbR9PmfD6uS2cToS4yG8nXsd8zSfVlussvX43m6XB60bZanVYDtbfKkyHtJqMeupI6BeWGZsucP1cwABq9BM"
credential = "{0}:{1}".format(client_id, secret)
print(base64.b64encode(credential.encode("utf-8")))