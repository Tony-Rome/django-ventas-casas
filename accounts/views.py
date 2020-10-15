from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

User = get_user_model() #Ocupa como modelo de auth por defecto UserAccount, definido al final de settings.py

class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None): #Pasa la data desde el formulario
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email ya existente'})
            else:
                if len(password) < 6 :
                    return Response({'error': 'Password mínimo 6 caracteres'})
                else:
                    user = User.objects.create_user(email=email, password=password, name=name)
                    user.save()
                    return Response({'success': 'Usuario creado con éxito'})
        
        else:
            return Response({'error': 'Contraseñas deben coincidir'})
