from django.urls import path
from .views import RegisterView
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

urlpatterns = router.urls + [
    path('api/register/', RegisterView.as_view(), name='register'),  # Keep the register route here
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  


]
