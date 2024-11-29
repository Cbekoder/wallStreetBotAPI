from django.views.generic import CreateView
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MemberResults, Members
from .serializers import MemberResultsSerializer, MemberRegistrationSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import get_object_or_404

class MemberRegistrationView(CreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberRegistrationSerializer


class CheckPhoneNumberAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'phone_number', openapi.IN_QUERY,
                description="Phone number",
                type=openapi.TYPE_STRING,
                required=True
            )
        ]
    )
    def get(self, request):
        phone_number = request.query_params.get('phone_number')
        if phone_number:
            member = Members.objects.filter(phone_number=phone_number).first()
            if member:
                return Response({"exists": True}, status=status.HTTP_200_OK)
            else:
                return Response({"exists": False}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST)


class MemberResultsView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'Telegram-Id', openapi.IN_QUERY,
                description="Telegram user ID",
                type=openapi.TYPE_STRING,
                required=True
            )
        ]
    )
    def get(self, request):
        telegram_id = request.query_params.get('Telegram-Id')
        results = MemberResults.objects.filter(member_id=telegram_id).order_by('-created_at')
        serializer = MemberResultsSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)