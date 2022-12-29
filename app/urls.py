from django.urls import path
from app.views import *
app_name="wert"

urlpatterns=[
    path('user/',user,name='user'),
    path('user1/',user1,name='user1')
]