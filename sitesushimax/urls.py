from django.urls import path
from sitesushimax.views import IndexPage

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
]
