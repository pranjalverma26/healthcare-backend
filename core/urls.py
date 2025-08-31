from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterAPIView, DoctorViewSet, PatientViewSet, MappingCreateListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'patients', PatientViewSet, basename='patient')

urlpatterns = [
    path('auth/register/', RegisterAPIView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
    path('mappings/', MappingCreateListView.as_view()),
]
