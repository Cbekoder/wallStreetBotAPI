from django.urls import path
from .views import *

urlpatterns = [
    path('register/', MemberRegistrationView.as_view(), name='member-registration'),
    path('check_phone/', CheckPhoneNumberAPIView.as_view(), name='check-phone-number'),
    path('results/', MemberResultsView.as_view(), name='member-results'),
]