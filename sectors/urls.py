from django.urls import path

from .views import index, user_sectors

urlpatterns = [
    path('', index, name='index'),
    path('<str:username>', user_sectors, name='user-sectors')
]
