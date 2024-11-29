from django.urls import path
from .views import *

urlpatterns = [
    path('register/', MemberRegistrationView.as_view(), name='member-registration'),
    path('check_phone/', CheckPhoneNumberAPIView.as_view(), name='check-phone-number'),
    path('save_result/', SaveResultView.as_view(), name='save-result'),
    path('results/', MemberResultsView.as_view(), name='member-results'),
]