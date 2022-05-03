from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.mail import send_mail

from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from .models import User
from .serializers import UserSerializer

from .utils import token_generator

BASE_FRONT_URL = 'http://localhost:3000'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['id'] = user.id
        token['email'] = user.email
        token['firstName'] = user.first_name
        token['lastName'] = user.last_name
        token['phoneNumber'] = user.phone_number
        token['profilePicture'] = user.profile_picture.__str__()
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def register(request):
    email_subject = 'User Account Activation ❤️'
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        user = user_serializer.save()
        print(user.id)
        print(user_serializer.data["email"])
        activate_url = mail_activation_link(request, user)
        email_body = f"Hi {user.first_name} {user.last_name} \n Please Use this link to verify your account \n {activate_url}"
        send_mail(
            subject=email_subject,
            message=email_body,
            from_email='noreply@crowd.com',
            recipient_list=[user_serializer.data["email"]],
        )
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def mail_activation_link(request, user):
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    domain = get_current_site(request).domain
    link = reverse('activate', kwargs={
        'uidb64': uidb64,
        'token': token_generator.make_token(user)
    })
    return f'http://{domain}{link}'


@api_view(['GET'])
def activate(request, uidb64, token):
    id = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=id)
    if not token_generator.check_token(user, token) or user.is_active:
        print(f'{BASE_FRONT_URL}/auth/login?message="Account Already Activated"')
        return HttpResponseRedirect(f'{BASE_FRONT_URL}/auth/login?message="Account Already Activated"')
    user.is_active = True
    user.save()
    return HttpResponseRedirect(f'{BASE_FRONT_URL}/auth/login?message="Account Activated Successfully"')
