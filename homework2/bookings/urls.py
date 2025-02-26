from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from bookings.views import MovieViewSet, SeatViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'api/movies', MovieViewSet)
router.register(r'api/seats', SeatViewSet)
router.register(r'api/bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Add this line

    path('', include('bookings.urls')),
    path('', include(router.urls)),
]