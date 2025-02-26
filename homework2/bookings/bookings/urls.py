from django.urls import path, include
from . import views
from django.contrib import admin, auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.movie_list, name='movie_list'),
    
    path('book/<int:movie_id>/', views.book_seat, name='book_seat'),
    path('booking_history/', views.booking_history, name='booking_history'),
]
