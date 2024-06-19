# # tasks.py
# from celery import shared_task
# from .models import OtpToken
# from datetime import datetime, timedelta

# @shared_task
# def delete_expired_otps():
#     expiration_time = datetime.now() - timedelta(minutes=2)
#     OtpToken.objects.filter(otp_created_at__lt=expiration_time).delete()
