from rest_framework import generics

from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data.pop('password')
        user = serializer.save()
        user.set_password(password)
        user.save()
