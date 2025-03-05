from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from ..models import Movie, Seat, Booking

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie description",
            release_date=date(2023, 1, 1),
            duration=120
        )
    
    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(Movie.objects.count(), 1)


class BookingProcessTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie description",
            release_date=date(2023, 1, 1),
            duration=120
        )
        for i in range(1, 101):
            Seat.objects.create(seat_number=str(i))
    
    def test_noseat(self):
        response = self.client.post(reverse('book_seat', args=[self.movie.id]), {})
        self.assertContains(response, "Please select a seat.")
    
    def test_taken(self):
        seat = Seat.objects.first()
        seat.is_booked = True
        seat.save()
        response = self.client.post(reverse('book_seat', args=[self.movie.id]), {'seat': seat.id})
        self.assertContains(response, "This seat has already been taken.")
    
    def test_succ(self):
        seat = Seat.objects.first()
        response = self.client.post(reverse('book_seat', args=[self.movie.id]), {'seat': seat.id})
        self.assertEqual(response.status_code, 302)
        booking = Booking.objects.get(seat=seat)
        self.assertEqual(booking.movie, self.movie)
        self.assertEqual(booking.user, self.user)
    
    def test_view(self):
        seat = Seat.objects.first()
        seat.is_booked = True
        seat.save()
        Booking.objects.create(movie=self.movie, seat=seat, user=self.user)
        response = self.client.get(reverse('booking_history'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.movie.title)
