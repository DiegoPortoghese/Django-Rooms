
from accounts.forms import CustomPasswordResetForm
from rest_auth.serializers import PasswordResetSerializer
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.forms import ResetPasswordForm
from django.conf import settings
from rest_framework import serializers
from accounts.models import Profile
from django.contrib.auth.models import User
from django.core import serializers as djangoSerializers


class CustomPasswordResetSerializer(PasswordResetSerializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    password_reset_form_class = CustomPasswordResetForm


class CustomRegisterSerializer(RegisterSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password1 = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
        }


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    
    def get_profile(self, data):
        profile = djangoSerializers.serialize("python", [ data.profile ])
        return profile
    
    class Meta:
        model = User
        fields = ('email', 'username' , 'first_name', 'last_name', 'profile')
        read_only_fields = ('email',)


