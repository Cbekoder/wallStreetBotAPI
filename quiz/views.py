from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from user.models import Members
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
                'telegram_id', openapi.IN_HEADER,
                description="Telegram user ID",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                'level', openapi.IN_HEADER,
                description="Level ID",
                type=openapi.TYPE_NUMBER,
                required=True
            ),
        ]
    )
    def get(self, request):
        telegram_id = request.headers.get('telegram_id')
        level = request.headers.get('level')
        level_instance = get_object_or_404(Level, pk=level)

        if not telegram_id or not level:
            return Response({"error": "telegram_id and level headers are required"}, status=status.HTTP_400_BAD_REQUEST)
        member = get_object_or_404(Members, telegram_id=telegram_id)
        if member:
            questions = Question.objects.filter(level=level_instance).order_by("?")[:20]
            quiz_data = {
                "level": level_instance.name,
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

class CheckAnswersView(APIView):
    def post(self, request):
        telegram_id = request.data.get('telegram_id')
        user_answers = request.data.get('answers', [])
        correct_answers = 0
        total_questions = len(user_answers)

        if total_questions == 0:
            return Response(
                {"error": "No answers provided."},
                status=status.HTTP_400_BAD_REQUEST
            )

        for answer in user_answers:
            question_id = answer.get('question_id')
            selected_option_id = answer.get('selected_option_id')

            if not question_id or not selected_option_id:
                return Response(
                    {"error": f"Invalid data for question_id: {question_id}."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            try:
                question = Question.objects.get(id=question_id)
                selected_option = Option.objects.get(id=selected_option_id, question=question)

                if selected_option.is_correct:
                    correct_answers += 1

            except Question.DoesNotExist:
                return Response(
                    {"error": f"Question with id {question_id} not found."},
                    status=status.HTTP_404_NOT_FOUND
                )
            except Option.DoesNotExist:
                return Response(
                    {"error": f"Option with id {selected_option_id} not found for question {question_id}."},
                    status=status.HTTP_404_NOT_FOUND
                )

        score = (correct_answers / total_questions) * 100

        return Response({
            "telegram_id": telegram_id,
            "correct_answers": correct_answers,
            "total_questions": total_questions,
            "score": score
        }, status=status.HTTP_200_OK)

