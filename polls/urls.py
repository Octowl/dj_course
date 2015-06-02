from django.conf.urls import url
from polls import views

urlpatterns = [
    url(r'^list/', views.poll_list, name='poll_list'),
]
