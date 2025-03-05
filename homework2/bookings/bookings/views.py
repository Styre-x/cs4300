from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from .models import Movie, Seat, Booking
from django.shortcuts import render, get_object_or_404, redirect

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie, Booking, Seat

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

@login_required
def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all().order_by('id') 
    seat_list = list(seats)
    seat_rows = [seat_list[i:i+10] for i in range(0, len(seat_list), 10)]
    
    error_message = None
    if request.method == 'POST':
        seat_id = request.POST.get('seat')
        if not seat_id:
            error_message = "Please select a seat."
        else:
            seat = get_object_or_404(Seat, id=seat_id)
            if seat.is_booked:
                error_message = "This seat has already been taken."
            else:
                seat.is_booked = True
                seat.save()
                Booking.objects.create(movie=movie, seat=seat, user=request.user)
                return redirect('booking_history')
    
    context = {
        'movie': movie,
        'seat_rows': seat_rows,
        'error_message': error_message,
    }
    return render(request, 'bookings/seat_booking.html', context)

@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})
