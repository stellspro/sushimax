"""sushimax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from sushimax import settings
from sitesushimax.views import ProductViewSet, PizzaViewSet, SushiViewSet, SnacksViewSet, SaladsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'pizza', PizzaViewSet)
router.register(r'sushi', SushiViewSet)
router.register(r'snacks', SnacksViewSet)
router.register(r'salads', SaladsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sitesushimax.urls')),
    path('api/get-products/', include(router.urls)),
    # path('api/get-salads/', show_salads),
    # path('api/v1/products/<int:pk>/', ProductViewSet.as_view({'put': 'update'})),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
