"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

from .views import (
    ActivityViewSet,
    LeaderboardViewSet,
    TeamViewSet,
    UserViewSet,
    WorkoutViewSet,
    api_root,
    router,
)

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

# Keep as module-level setting for docs/debug visibility.
API_BASE_URL = f"{base_url}/api"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/activities', ActivityViewSet.as_view({'get': 'list'}), name='activities-list-no-slash'),
    path('api/leaderboard', LeaderboardViewSet.as_view({'get': 'list'}), name='leaderboard-list-no-slash'),
    path('api/teams', TeamViewSet.as_view({'get': 'list'}), name='teams-list-no-slash'),
    path('api/users', UserViewSet.as_view({'get': 'list'}), name='users-list-no-slash'),
    path('api/workouts', WorkoutViewSet.as_view({'get': 'list'}), name='workouts-list-no-slash'),
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(pattern_name='api-root', permanent=False)),
]
