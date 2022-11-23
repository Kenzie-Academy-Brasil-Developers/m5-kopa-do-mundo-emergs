from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from teams.models import Team


class TeamView(APIView):
    def post(self, request):
        team_data = request.data
        team = Team.objects.create(
            name=team_data["name"],
            titles=team_data["titles"],
            top_scorer=team_data["top_scorer"],
            fifa_code=team_data["fifa_code"],
            founded_at=team_data["founded_at"],
        )
        return Response(model_to_dict(team), 201)

    def get(self, request):
        teams = Team.objects.all()
        teams_dict = []

        for team in teams:
            teams_dict.append(model_to_dict(team))

        return Response(teams_dict, 200)
