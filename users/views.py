from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.mail import send_mail

from .serializers import UserSerializer

EMAIL_SUBJECT = 'User Account Activation ❤️'
EMAIL_MESSAGE = 'Please activate your account via this link 🤌'


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
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        # user_serializer.save()
        print(user_serializer.data["email"])
        send_mail(
            subject=EMAIL_SUBJECT,
            message=EMAIL_MESSAGE,
            from_email='noreply@crowd.com',
            recipient_list=[user_serializer.data["email"]],
        )
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


