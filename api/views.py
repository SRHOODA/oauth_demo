from rest_framework.views import APIView
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework.permissions import IsAuthenticated

class HelloApiView(APIView):
    # Must be authenticated + have the "read" scope:
    permission_classes = [IsAuthenticated, TokenHasScope]
    required_scopes = ["read"]

    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}!"})


#!#!client creds(auth type)
# from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
# from rest_framework.views import APIView
# from rest_framework.response import Response

# class HelloApiView(APIView):
#     authentication_classes = [OAuth2Authentication]
#     permission_classes = [TokenHasScope]      # removed IsAuthenticated
#     required_scopes = ["read"]

#     def get(self, request):
#         who = getattr(request, "user", None)
#         name = getattr(who, "username", None) or "app-client"
#         return Response({"message": f"Hello, {name}!"})
