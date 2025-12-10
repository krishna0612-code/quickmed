
  

# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("Email is required")

#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_active", True)

#         return self.create_user(email, password, **extra_fields)


# class User(AbstractBaseUser, PermissionsMixin):
#     fullName = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=15)
#     userType = models.CharField(max_length=20)

#     # 🟢 PATIENT EXTRA FIELDS
#     dateOfBirth = models.DateField(null=True, blank=True)
#     gender = models.CharField(max_length=20, null=True, blank=True)
#     address = models.TextField(null=True, blank=True)
#     emergencyContact = models.CharField(max_length=20, null=True, blank=True)
#     linkedAccounts = models.JSONField(default=list, blank=True)

#     # 🟡 DELIVERY PARTNER FIELDS
#     vehicleType = models.CharField(max_length=50, null=True, blank=True)
#     vehicleNumber = models.CharField(max_length=50, null=True, blank=True)
#     idProof = models.CharField(max_length=50, null=True, blank=True)
#     idNumber = models.CharField(max_length=50, null=True, blank=True)
#     availability = models.CharField(max_length=50, null=True, blank=True)

#     # 🔵 DOCTOR FIELDS
#     specialization = models.CharField(max_length=50, null=True, blank=True)
#     medicalLicense = models.CharField(max_length=50, null=True, blank=True)
#     qualifications = models.TextField(null=True, blank=True)
#     experience = models.IntegerField(null=True, blank=True)
#     consultationFee = models.IntegerField(null=True, blank=True)
#     availableHours = models.TextField(null=True, blank=True)

#     # 🟣 VENDOR FIELDS
#     storeName = models.CharField(max_length=200, null=True, blank=True)
#     businessType = models.CharField(max_length=50, null=True, blank=True)
#     gstNumber = models.CharField(max_length=30, null=True, blank=True)
#     storeAddress = models.TextField(null=True, blank=True)
#     businessLicense = models.CharField(max_length=100, null=True, blank=True)

#     # DJANGO REQUIRED
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)

#     isVerified = models.BooleanField(default=False)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["fullName"]

#     objects = UserManager()

#     def __str__(self):
#         return self.email



from django.db import models
from django.contrib.auth.hashers import make_password


# -------------------------------------
# 🟢 PATIENT TABLE
# -------------------------------------
class PatientUser(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)

    dateOfBirth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    emergencyContact = models.CharField(max_length=20, null=True, blank=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return f"Patient - {self.fullName}"


# -------------------------------------
# 🔵 DOCTOR TABLE
# -------------------------------------
class DoctorUser(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)

    specialization = models.CharField(max_length=50)
    medicalLicense = models.CharField(max_length=50)
    qualifications = models.TextField()
    experience = models.IntegerField()
    consultationFee = models.IntegerField()
    availableHours = models.TextField()

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return f"Doctor - {self.fullName}"


# -------------------------------------
# 🟡 VENDOR TABLE
# -------------------------------------
class VendorUser(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)

    storeName = models.CharField(max_length=200)
    businessType = models.CharField(max_length=50)
    gstNumber = models.CharField(max_length=30)
    storeAddress = models.TextField()
    businessLicense = models.CharField(max_length=100)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return f"Vendor - {self.storeName}"


# -------------------------------------
# 🟣 DELIVERY PARTNER TABLE
# -------------------------------------
class DeliveryUser(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)

    vehicleType = models.CharField(max_length=50)
    vehicleNumber = models.CharField(max_length=50)
    idProof = models.CharField(max_length=50)
    idNumber = models.CharField(max_length=50)
    availability = models.CharField(max_length=50)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return f"Delivery Partner - {self.fullName}"
