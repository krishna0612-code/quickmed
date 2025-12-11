



# from rest_framework import serializers
# from .models import User

# class SignupSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = "__all__"   # <-- this makes ALL fields save
#         extra_kwargs = {
#             "password": {"write_only": True},
#         }

#     def create(self, validated_data):
#         password = validated_data.pop("password")
#         user = User.objects.create(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user

from rest_framework import serializers
from .models import (
    PatientUser,
    DoctorUser,
    VendorUser,
    DeliveryUser
)

# class SignupSerializer(serializers.Serializer):
#     fullName = serializers.CharField()
#     email = serializers.EmailField()
#     phone = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#     userType = serializers.CharField()   # user / doctor / vendor / delivery

#     # Extra fields (optional)
#     specialization = serializers.CharField(required=False)
#     medicalLicense = serializers.CharField(required=False)
#     qualifications = serializers.CharField(required=False)
#     experience = serializers.IntegerField(required=False)
#     consultationFee = serializers.IntegerField(required=False)
#     availableHours = serializers.CharField(required=False)

#     vehicleType = serializers.CharField(required=False)
#     vehicleNumber = serializers.CharField(required=False)
#     idProof = serializers.CharField(required=False)
#     idNumber = serializers.CharField(required=False)
#     availability = serializers.CharField(required=False)

#     storeName = serializers.CharField(required=False)
#     businessType = serializers.CharField(required=False)
#     gstNumber = serializers.CharField(required=False)
#     storeAddress = serializers.CharField(required=False)
#     businessLicense = serializers.CharField(required=False)

#     def create(self, validated_data):
#         userType = validated_data.pop("userType")
#         password = validated_data.pop("password")

#         # PATIENT USER
#         if userType == "user":
#             user = PatientUser(**validated_data)
#             user.set_password(password)
#             user.save()
#             return user

#         # DOCTOR USER
#         if userType == "doctor":
#             user = DoctorUser(**validated_data)
#             user.set_password(password)
#             user.save()
#             return user

#         # VENDOR USER
#         if userType == "vendor":
#             user = VendorUser(**validated_data)
#             user.set_password(password)
#             user.save()
#             return user

#         # DELIVERY USER
#         if userType == "delivery":
#             user = DeliveryUser(**validated_data)
#             user.set_password(password)
#             user.save()
#             return user

#         raise serializers.ValidationError("Invalid userType")


# class SignupSerializer(serializers.Serializer):
#     fullName = serializers.CharField()
#     email = serializers.EmailField()
#     phone = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#     userType = serializers.CharField()

#     # Delivery fields
#     aadharNumber = serializers.CharField(required=False)
#     panNumber = serializers.CharField(required=False)
#     vehicleNumber = serializers.CharField(required=False)
#     drivingLicenseNumber = serializers.CharField(required=False)

#     # File uploads
#     aadharFront = serializers.ImageField(required=False)
#     aadharBack = serializers.ImageField(required=False)
#     panCard = serializers.ImageField(required=False)
#     drivingLicenseFront = serializers.ImageField(required=False)
#     drivingLicenseBack = serializers.ImageField(required=False)
#     vehicleRC = serializers.ImageField(required=False)
#     livePhoto = serializers.ImageField(required=False)

#     # Vendor fields
#     storeName = serializers.CharField(required=False)
#     businessType = serializers.CharField(required=False)
#     gstNumber = serializers.CharField(required=False)
#     storeAddress = serializers.CharField(required=False)
#     businessLicense = serializers.CharField(required=False)

#     # Doctor fields
#     specialization = serializers.CharField(required=False)
#     medicalLicense = serializers.CharField(required=False)
#     qualifications = serializers.CharField(required=False)
#     experience = serializers.IntegerField(required=False)
#     consultationFee = serializers.IntegerField(required=False)
#     availableHours = serializers.CharField(required=False)

#     def create(self, validated_data):
#         userType = validated_data.pop("userType")
#         password = validated_data.pop("password")

#         # DELIVERY USER
#         if userType == "delivery":
#             user = DeliveryUser(**validated_data)
#             user.set_password(password)
#             user.save()
#             return user

#         # PATIENT USER
#         if userType == "user":
#             user = PatientUser(**validated_data)
#             user.set_password(password)
#             user.save()
#             return user

#         # DOCTOR USER
#         if userType == "doctor":
#             user = DoctorUser(**validated_data)
#             user.set_password(password)
#             user.save()
#             return user

#         # VENDOR USER
#         if userType == "vendor":
#             user = VendorUser(**validated_data)
#             user.set_password(password)
#             user.save()
#             return user

#         raise serializers.ValidationError("Invalid userType")
class SignupSerializer(serializers.Serializer):
    fullName = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)
    userType = serializers.CharField()

    # Patient fields
   # Patient fields
    dateOfBirth = serializers.DateField(required=False)
    gender = serializers.CharField(required=False)
    deliveryAddress = serializers.CharField(required=False)
    emergencyContact = serializers.CharField(required=False)

    # Delivery fields (no change)
    aadharNumber = serializers.CharField(required=False)
    panNumber = serializers.CharField(required=False)
    vehicleNumber = serializers.CharField(required=False)
    drivingLicenseNumber = serializers.CharField(required=False)

    # Vendor fields…
    # Doctor fields…
    # Images…

    def create(self, validated_data):
        userType = validated_data.pop("userType")
        password = validated_data.pop("password")

        # PATIENT USER
        if userType == "user":
    # Map deliveryAddress → address
            validated_data["address"] = validated_data.pop("deliveryAddress", None)

            user = PatientUser(**validated_data)
            user.set_password(password)
            user.save()
            return user

        # DELIVERY USER
        if userType == "delivery":
            user = DeliveryUser(**validated_data)
            user.set_password(password)
            user.save()
            return user

        # DOCTOR USER
        if userType == "doctor":
            user = DoctorUser(**validated_data)
            user.set_password(password)
            user.save()
            return user

        # VENDOR USER
        if userType == "vendor":
            user = VendorUser(**validated_data)
            user.set_password(password)
            user.save()
            return user

        raise serializers.ValidationError("Invalid userType")
