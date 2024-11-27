from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Level, Question, Option
from .serializers import LevelSerializer
import random


class LevelsView(ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer



class GetQuizView(APIView):
    def get(self, request, level):
        level_instance = get_object_or_404(Level, pk=level)

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
                "options": [{"id": option.id, "text": option.text} for option in options_list]
            })

        return Response(quiz_data, status=status.HTTP_200_OK)

class CheckAnswersView(APIView):
    def post(self, request):
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
            "correct_answers": correct_answers,
            "total_questions": total_questions,
            "score": score
        }, status=status.HTTP_200_OK)

