from django.urls import path, include
from rest_framework import routers

from .views import PatternViewSet

router = routers.DefaultRouter()
router.register('pattern', PatternViewSet)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('rest_framework.urls')),
]

urlpatterns += router.urls

# /api/auth/users/ post-запрос - регистрация юзера
# /api/auth/token/login - получить токен для авторизации через ПО
# /api/login/ - авторизация через браузер
# /api/pattern/ - список паттернов
# /api/pattern/<pk>/generation/ - post-запрос - генерация сообщения