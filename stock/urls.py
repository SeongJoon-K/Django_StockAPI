from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home, name='home'), # 127.0.0.0.0: 일떄
]
