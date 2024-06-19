from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import OtpToken
from .serializers import OtpSerializer 
from django.core.mail import EmailMessage
# from otpApp.settings import EMAIL_HOST_USER
from django.conf import settings


# Create your views here.
class TestOtpView(APIView):

    def post(self, request):
        
        try:
            data = request.data
            email = request.data['email'] 
            name = request.data['name'] 
            otp = request.data['otp'] 

            item = OtpSerializer(data=data)        


            if not item.is_valid():
                return Response({'data': item.errors, 'message': "Something went wrong" }, status= status.HTTP_400_BAD_REQUEST)
            
            # Check if an OTP for this email already exists and if it's expired
            existing_otp = OtpToken.objects.filter(email=email).first()
            if existing_otp and not existing_otp.is_expired():
                return Response({'status': 'error', 'message': "An OTP was recently sent, please wait before requesting a new one."}, status=status.HTTP_400_BAD_REQUEST)
            

            # Delete the old OTP if it exists
            if existing_otp:
                existing_otp.delete()


            subject="One time pass-code for Email verification"
            from_email=settings.EMAIL_HOST_USER
            to_email=email
            html_content = f"""
            <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; color: #333; margin: 0; padding: 0;">
                <div style="width: 100%; max-width: 600px; margin: 0 auto; padding: 20px; background-color: #ffffff; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
                    <h1 style="font-size: 24px; margin-bottom: 20px;">Your OTP Code</h1>
                    <p style="font-size: 16px; margin-bottom: 10px;">Dear {name},</p>
                    <p style="font-size: 16px; margin-bottom: 10px;">Your one-time password (OTP) for completing your signup is: </p>
                    <div style="display: inline-block; font-size: 24px; font-weight: bold; padding: 10px 20px; border-radius: 5px; background-color: #e0e0e0; margin: 20px 0;">{otp}</div>
                    <p style="font-size: 16px; margin-bottom: 10px;">Please use this code to complete your registration. This code is valid for the next 2 minutes.</p>
                    <p style="font-size: 16px; margin-bottom: 10px;">If you did not request this code, please ignore this message.</p>
                    <div style="font-size: 14px; color: #777; margin-top: 20px;">
                        <p>Thank you,<br> Spiritan</p>
                    </div>
                </div>
            </body>
            """

            email = EmailMessage(subject, html_content, from_email, to=[to_email])
            email.content_subtype = "html"  # Set the email content type to HTML
            email.send(fail_silently=False)

            # Create and save the new OTP
            item.save()
            
            return Response({'status': 'success', 'data': item.data, 'message': "New order created or placed"}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'status': 'error', 'message': f"Something went wrong: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'status': 'error', 'message': "Something went wrong in creation of Order" }, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            # Delete all records in the OtpToken model
            OtpToken.objects.all().delete()
            return Response({'status': 'success', 'message': 'All OTP tokens deleted successfully.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': 'error', 'message': f"Something went wrong: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)