from django.urls import path
from .views import TestOtpView


urlpatterns = [
    path('send/', TestOtpView.as_view(), name='email-sender'),
    # path('user_profile/', RetrieveUserView.as_view(), name='user-list')
]
