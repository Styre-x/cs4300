from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test Description",
            release_date="2025-01-01",
            duration=120
        )

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Test Movie")

#TODO: add more tests
