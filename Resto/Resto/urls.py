from django.conf.urls import include, url
from django.contrib import admin
from core.views import *


urlpatterns = [
#     Examples:
#     url(r'^$', 'Resto.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home', Home.as_view()),
<<<<<<< HEAD
    url(r'^carta/(?P<seccion_show>\w+)', CartaView.as_view())
=======
<<<<<<< HEAD
    url(r'^carta', CartaView.as_view()),
    url(r'^descanso', DescansoView.as_view())
]
=======
    url(r'^carta', CartaView.as_view())
>>>>>>> ac0455819dabdf18b51a0f1abbb5bfbb4d4b0741
]
>>>>>>> 653547a8bb55fbe5db8110da299776d9dc3c5d13
