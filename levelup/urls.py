"""
URL configuration for levelup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls import include
from rest_framework import routers
from levelupapi.views import GameTypeView, EventView
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypeView, 'gametype')
router.register(r'events', EventView, 'event')
# The first parameter, r'gametypes, is setting up the url.
# The second GameTypeView is telling the server which view to use when it sees that url.
# The third, gametype, is called the base name. You’ll only see the base name if you get an error in the server. It acts as a nickname for the resource and is usually the singular version of the url.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
