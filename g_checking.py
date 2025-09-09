#!run this in sheel to see output

# from oauth2_provider.models import AccessToken
# t = AccessToken.objects.get(token="1pVdO8AWHkZf2gAywGdxPBLFVKolZo")
# print("user:", t.user)       # should be your login user for Auth Code flow
# print("scopes:", t.scope)    # should contain "read"
# print("expires:", t.expires)
# print("grant:", t.application.authorization_grant_type)



import os
import sys
import django

# 1) Ensure Python can find your project package (folder that has settings.py inside <project>/settings.py)
# If new.py sits next to manage.py, you can skip sys.path bits.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# 2) Point to your settings module, e.g. "authserver.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# 3) Initialize Django
django.setup()

# 4) Now import and use Django models
from oauth2_provider.models import AccessToken

t = AccessToken.objects.get(token="1pVdO8AWHkZf2gAywGdxPBLFVKolZo")
print("user:", t.user)
print("scopes:", t.scope)
print("expires:", t.expires)
print("grant:", t.application.authorization_grant_type)
