from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView, PatientViewSet, DoctorViewSet, PatientDoctorMappingViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'mappings', PatientDoctorMappingViewSet, basename='mapping')

urlpatterns = [
    path('auth/register/', UserRegistrationView.as_view(), name='user-register'),
    path('', include(router.urls)),
]
