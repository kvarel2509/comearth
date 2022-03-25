from django.urls import path, include


urlpatterns = [
    # энд-поинт для входа через браузер
    path('login/', include('rest_framework.urls')),
    # энд-поинт для входа через ПО.
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]