from django.urls import path
from sitesushimax.views import IndexPage, PizzaPage, SushiPage, SnacksPage, SaladsPage, CartPage, OrderingPage, checkout

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
    path('pizza/', PizzaPage.as_view(), name='pizza_page'),
    path('sushi/', SushiPage.as_view(), name='sushi_page'),
    path('snacks/', SnacksPage.as_view(), name='snacks_page'),
    path('salads/', SaladsPage.as_view(), name='salads_page'),
    path('my_cart/', CartPage.as_view(), name='cart_page'),
    path('order_page/', checkout, name='order_page'),

]
