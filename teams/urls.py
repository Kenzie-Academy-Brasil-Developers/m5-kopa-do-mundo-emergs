from django.urls import path
from .views import TeamView, TeamViewId

urlpatterns = [
    path("teams/", TeamView.as_view()),
    path("teams/<int:id>/", TeamViewId.as_view()),
]
