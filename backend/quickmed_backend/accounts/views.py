


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import User
# from .serializers import SignupSerializer
# from django.contrib.auth.hashers import check_password
# import random

# # ------------------------------------
# # SIGNUP (already done by you)
# # ------------------------------------
# @api_view(["POST"])
# def signup(request):
#     serializer = SignupSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "User registered successfully"}, status=201)
#     return Response(serializer.errors, status=400)


# # ------------------------------------
# # EMAIL LOGIN
# # ------------------------------------
# @api_view(["POST"])
# def email_login(request):
#     email = request.data.get("email")
#     password = request.data.get("password")
#     userType = request.data.get("userType")

#     try:
#         user = User.objects.get(email=email, userType=userType)
#     except User.DoesNotExist:
#         return Response({"message": "Invalid login"}, status=400)

#     if not check_password(password, user.password):
#         return Response({"message": "Invalid credentials"}, status=400)

#     return Response({
#         "message": "Login successful",
#         "user": {
#             "fullName": user.fullName,
#             "email": user.email,
#             "phone": user.phone,
#             "userType": user.userType
#         }
#     }, status=200)


# # ------------------------------------
# # SEND OTP
# # ------------------------------------



# # @api_view(["POST"])
# # def send_otp(request):
# #     phone = request.data.get("phone")

# #     # ✔ Send OTP ONLY for userType = Patient (normal user)
# #     user_exists = User.objects.filter(phone=phone, userType="user").exists()

# #     if not user_exists:
# #         return Response(
# #             {"message": "This phone number is not registered as a Patient user"},
# #             status=400
# #         )

# #     # Generate OTP
# #     otp = str(random.randint(100000, 999999))

# #     # Save OTP in session
# #     request.session[f"otp_{phone}"] = otp

# #     # Return in response
# #     return Response({
# #         "message": "OTP sent successfully",
# #         "phone": phone,
# #         "otp": otp
# #     }, status=200)

# @api_view(["POST"])
# def send_otp(request):
#     phone = request.data.get("phone")

#     # Check if user exists with correct userType
#     user_exists = User.objects.filter(phone=phone, userType="user").exists()

#     if not user_exists:
#         return Response(
#             {"message": "This phone number is not registered as a Patient user"},
#             status=400
#         )

#     # Generate OTP
#     otp = str(random.randint(1000, 9999))
#     print("🎯 OTP for", phone, "is:", otp)

#     # Save OTP to session
#     request.session[f"otp_{phone}"] = otp

#     # Return OTP in API output
#     return Response({
#         "message": "OTP sent successfully",
#         "phone": phone,
#         "otp": otp     # 👈 OTP visible here
#     }, status=200)



# # ------------------------------------
# # VERIFY OTP
# # ------------------------------------
# @api_view(["POST"])
# def verify_otp(request):
#     phone = request.data.get("phone")
#     otp = request.data.get("otp")
#     userType = request.data.get("userType")

#     saved_otp = request.session.get(f"otp_{phone}")

#     if saved_otp != otp:
#         return Response({"message": "Invalid OTP"}, status=400)

#     try:
#         user = User.objects.get(phone=phone, userType=userType)
#     except User.DoesNotExist:
#         return Response({"message": "User not found"}, status=400)

#     return Response({
#         "message": "Login successful",
#         "user": {
#             "fullName": user.fullName,
#             "email": user.email,
#             "phone": user.phone,
#             "userType": user.userType
#         }
#     }, status=200)




from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import SignupSerializer

from .models import (
    PatientUser,
    DoctorUser,
    VendorUser,
    DeliveryUser
)

from django.contrib.auth.hashers import check_password
import random


# ------------------------------------
# 🟢 SIGNUP (Works for all 4 user types)
# ------------------------------------
@api_view(["POST"])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()
        return Response({"message": "User registered successfully"}, status=201)

    return Response(serializer.errors, status=400)



# ------------------------------------
# 🟡 EMAIL LOGIN (For all dashboards)
# ------------------------------------
@api_view(["POST"])
def email_login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    userType = request.data.get("userType")

    user = None

    # Check in correct table
    if userType == "user":
        user = PatientUser.objects.filter(email=email).first()

    elif userType == "doctor":
        user = DoctorUser.objects.filter(email=email).first()

    elif userType == "vendor":
        user = VendorUser.objects.filter(email=email).first()

    elif userType == "delivery":
        user = DeliveryUser.objects.filter(email=email).first()

    else:
        return Response({"message": "Invalid userType"}, status=400)

    if not user:
        return Response({"message": "Invalid login"}, status=400)

    if not check_password(password, user.password):
        return Response({"message": "Invalid credentials"}, status=400)

    return Response({
        "message": "Login successful",
        "user": {
            "fullName": user.fullName,
            "email": user.email,
            "phone": user.phone,
            "userType": userType
        }
    }, status=200)



# ------------------------------------
# 🔵 SEND OTP (ONLY Patients login through OTP)
# ------------------------------------
@api_view(["POST"])
def send_otp(request):
    phone = request.data.get("phone")

    # OTP login only allowed for patients/userType=user
    user = PatientUser.objects.filter(phone=phone).first()

    if not user:
        return Response(
            {"message": "This phone number is not registered as a Patient user"},
            status=400
        )

    # Generate OTP
    otp = str(random.randint(1000, 9999))
    
    print("🎯 OTP for", phone, "is:", otp)

    # Save OTP in session
    request.session[f"otp_{phone}"] = otp

    return Response({
        "message": "OTP sent successfully",
        "phone": phone,
        "otp": otp   # Visible in response
    }, status=200)



# ------------------------------------
# 🔴 VERIFY OTP (Only Patients)
# ------------------------------------
@api_view(["POST"])
def verify_otp(request):
    phone = request.data.get("phone")
    otp = request.data.get("otp")

    saved_otp = request.session.get(f"otp_{phone}")

    if saved_otp != otp:
        return Response({"message": "Invalid OTP"}, status=400)

    user = PatientUser.objects.filter(phone=phone).first()

    if not user:
        return Response({"message": "User not found"}, status=400)

    return Response({
        "message": "Login successful",
        "user": {
            "fullName": user.fullName,
            "email": user.email,
            "phone": user.phone,
            "userType": "user"
        }
    }, status=200)
