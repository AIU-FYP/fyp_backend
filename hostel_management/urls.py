from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, ProfileViewSet, CustomTokenObtainPairView
from students.views import StudentViewSet
from hostels.views import HostelViewSet, LevelViewSet, RoomViewSet, BedViewSet
from requests.views import MaintenanceRequestViewSet, ChangeRoomRequestViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'students', StudentViewSet)
router.register(r'hostels', HostelViewSet)
router.register(r'levels', LevelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'beds', BedViewSet, basename='bed')
router.register(r'maintenance-requests', MaintenanceRequestViewSet)
router.register(r'change-room-requests', ChangeRoomRequestViewSet)

urlpatterns = [
                  path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('admin/', admin.site.urls),
                  path('api/', include(router.urls)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
