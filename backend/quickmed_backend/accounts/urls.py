from django.urls import path
from .views import signup, email_login, send_otp, verify_otp, delivery_signup

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("delivery/signup/", delivery_signup, name="delivery_signup"),

    # Email Login (POST)
    path("login/email/", email_login, name="email_login"),

    # Send OTP (POST)
    path("login/sendotp/", send_otp, name="send_otp"),

    # Verify OTP (POST)
    path("login/verifyotp/", verify_otp, name="verify_otp"),
]
