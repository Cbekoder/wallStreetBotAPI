from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from user.models import Members, MemberResults
from .models import Level, Question, Option
from .serializers import LevelSerializer
import random


class LevelsView(ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer



class GetQuizView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'amount', openapi.IN_QUERY,
                description="Question amount",
                type=openapi.TYPE_NUMBER,
                required=True
            ),
            openapi.Parameter(
                'level', openapi.IN_QUERY,
                description="Level ID",
                type=openapi.TYPE_NUMBER,
                required=True
            ),
        ]
    )
    def get(self, request):
        level_id = request.query_params.get('level')
        amount = request.query_params.get("amount")
        amount = amount if 0 <= amount <= 50 else 50

        if not level_id:
            return Response({"error": "telegram_id and level headers are required"}, status=status.HTTP_400_BAD_REQUEST)

        level = get_object_or_404(Level, pk=level_id)

        questions = Question.objects.filter(level=level).order_by("?")[:amount]
        quiz_data = {
            "level": level.name,
            "questions": []
        }
        for question in questions:
            options = Option.objects.filter(question=question)
            options_list = list(options)
            random.shuffle(options_list)

            quiz_data["questions"].append({
                "question_id": question.id,
                "question": question.text,
                "options": [{"id": option.id, "text": option.text, "is_correct": option.is_correct} for option in options_list]
            })
        return Response(quiz_data, status=status.HTTP_200_OK)


