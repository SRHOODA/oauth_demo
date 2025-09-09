follow these steps defined in this link-

https://django-oauth-toolkit.readthedocs.io/en/latest/getting_started.html#oauth2-authorization-grants


A) Google

Go to Google Cloud Console → Credentials → Create Credentials → OAuth client ID.

Application type: Web application

Authorized redirect URIs:

http://127.0.0.1:8000/accounts/google/login/callback/

Save the Client ID and Client Secret.

B) GitHub

Go to GitHub → Settings → Developer settings → OAuth Apps → New OAuth App.

Homepage URL: http://127.0.0.1:8000/

Authorization callback URL: http://127.0.0.1:8000/accounts/github/login/callback/

Save the Client ID and Client Secret.


curl -X POST http://127.0.0.1:8000/o/token/ \                                                                           -H "Content-Type: application/x-www-form-urlencoded" \                                                                                                                          -d "grant_type=refresh_token" \
  -d "refresh_token=WZ9mkd90TQTdrOhSkPxxf9MwUMhtxt" \
  -d "client_id=ehMiCBpfvYXFa70KlDs7Nx5aZgAvEZZmQsKUCq4J" \
  -d "client_secret=c7F7fnFvz7Ez3oRVoth7bNznh4D5mvebWEljGLM0vcTrbbR9PmfD6uS2cToS4yG8nXsd8zSfVlussvX43m6XB60bZanVYDtbfKkyHtJqMeupI6BeWGZsucP1cwABq9BM"

define scope as well in here