from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework.views import APIView, status
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
        return Response(model_to_dict(team), status.HTTP_201_CREATED)

    def get(self, request):
        teams = Team.objects.all()
        teams_dict = []

        for team in teams:
            teams_dict.append(model_to_dict(team))

        return Response(teams_dict, status.HTTP_200_OK)


class TeamViewId(APIView):
    def get(self, request, id: int):
        try:
            team = Team.objects.get(pk=id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        return Response(model_to_dict(team))

    def delete(self, request, id: int):
        try:
            team = Team.objects.get(pk=id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id: int):
        try:
            team = Team.objects.get(pk=id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team.name = request.data.get("name", team.name)
        team.titles = request.data.get("titles", team.titles)
        team.top_scorer = request.data.get("top_scorer", team.top_scorer)
        team.fifa_code = request.data.get("fifa_code", team.fifa_code)
        team.founded_at = request.data.get("founded_at", team.founded_at)

        team.save()

        return Response(model_to_dict(team), status.HTTP_200_OK)
