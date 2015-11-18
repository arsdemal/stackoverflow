from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^question/$', views.question, name='question'),
    url(r'^main/$', views.main, name='main'),
    url(r'^addquestion/$', views.addquestion, name='addquestion'),
    url(r'^registration/$', views.registration, name='registration'),
]
