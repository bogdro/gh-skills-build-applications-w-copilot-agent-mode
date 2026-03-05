from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)
        Activity.objects.create(user=tony, type='Running', duration=30, date='2024-01-01')
        Workout.objects.create(name='Super Strength', description='Strength workout for heroes', suggested_for='Marvel')
        Leaderboard.objects.create(user=tony, score=100)

    def test_user_email_unique(self):
        marvel = Team.objects.get(name='Marvel')
        with self.assertRaises(Exception):
            User.objects.create(name='Duplicate', email='tony@marvel.com', team=marvel)

    def test_leaderboard_score(self):
        tony = User.objects.get(name='Tony Stark')
        entry = Leaderboard.objects.get(user=tony)
        self.assertEqual(entry.score, 100)
