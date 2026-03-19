from django.core.management.base import BaseCommand

from octofit_tracker.models import Activity, Leaderboard, Team, User, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data in dependency-safe order.
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Sample data
        users = [
            {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
            {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
        ]
        teams = [
            {"name": "Marvel", "members": ["Iron Man", "Captain America", "Black Widow"]},
            {"name": "DC", "members": ["Superman", "Batman", "Wonder Woman"]},
        ]
        activities = [
            {"user": "Superman", "activity": "Flying", "duration": 60},
            {"user": "Batman", "activity": "Martial Arts", "duration": 45},
            {"user": "Iron Man", "activity": "Flight Training", "duration": 50},
        ]
        leaderboard = [
            {"team": "Marvel", "points": 150},
            {"team": "DC", "points": 140},
        ]
        workouts = [
            {"name": "Strength Training", "suggested_for": ["Superman", "Iron Man"]},
            {"name": "Agility Drills", "suggested_for": ["Batman", "Black Widow"]},
        ]

        for user in users:
            User.objects.create(**user)
        for team in teams:
            Team.objects.create(**team)
        for activity in activities:
            Activity.objects.create(**activity)
        for row in leaderboard:
            Leaderboard.objects.create(**row)
        for workout in workouts:
            Workout.objects.create(**workout)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
