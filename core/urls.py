"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.views import HelloApiView

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Hi {request.user.get_username()}! <a href='/accounts/logout/'>Logout</a>")
    return HttpResponse("Hello! <a href='/accounts/login/'>Login</a>")




urlpatterns = [
    path('admin/', admin.site.urls),

    # OAuth 2.0 provider endpoints (authorize, token, revoke, etc.)
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),

    # allauth (login/signup/account/social)
    path("accounts/", include("allauth.urls")),

    # # your API
    # path("api/", include("api.urls")),

    # A sample protected API endpoint:
    path("api/hello/", HelloApiView.as_view(), name="hello"),
]
