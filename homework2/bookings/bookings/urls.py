from django.urls import path, include
from . import views
from django.contrib import admin, auth
from rest_framework import routers
from bookings.views import MovieViewSet, SeatViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.movie_list, name='movie_list'),
    path('api/', include(router.urls)),
    path('book/<int:movie_id>/', views.book_seat, name='book_seat'),
    path('booking_history/', views.booking_history, name='booking_history'),
]
