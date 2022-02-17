from django.urls import path
from sitesushimax.views import index

urlpatterns = [
    path('', index, name='home')
]
