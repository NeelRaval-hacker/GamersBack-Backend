from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from helpers.helper import parse_json

class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = json.loads(request.body)['email']
        if User.objects.filter(email=email).exists():
            raise SuspiciousOperation
        user = User()
        user.email = email
        user.username = uuid.uuid4()
        user.first_name = json.loads(request.body)['firstName']
        user.last_name = json.loads(request.body)['lastName']
        user.save()
        return Response({"status":200,"message":"Registered Succesfully"})
