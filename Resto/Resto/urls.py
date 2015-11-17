from django.conf.urls import include, url
from django.contrib import admin
from core.views import *


urlpatterns = [
#     Examples:
#     url(r'^$', 'Resto.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home', Home.as_view()),
    url(r'^carta', CartaView.as_view())
]
