from django.urls import path, include
from rest_framework import routers
from .views import PatternViewSet


router = routers.DefaultRouter()
router.register('pattern', PatternViewSet)

urlpatterns = [
    # энд-поинт для входа через браузер
    path('login/', include('rest_framework.urls')),
    # энд-поинт для входа через ПО.
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

]

urlpatterns += router.urls
