from django.urls import path
from app2.views import *
app_name="sdfg"

urlpatterns=[
    path('user2/',user2,name='user2'),
    path('user3/',user3,name='user3'),
]