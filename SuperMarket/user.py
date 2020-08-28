from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import *


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        addresses = [{'id': address.pk,
                      'address': address.address,
                      'postal_code': address.postal_code,
                      'city': address.city,
                      'country': address.country} for address in Addresses.objects.filter(user=user)]
        numbers = [{'id': number.pk,
                    'country_code': number.country_code,
                    'number': number.number} for number in Numbers.objects.filter(user=user)]
        orders = [{'id': order.pk} for order in Order.objects.filter(user=user)]
        return Response({
            'token': token.key,
            'last_login': user.last_login,
            'id': user.pk,
            'username': user.username,
            'media': user.media if user.media else None,
            'email': user.email,
            'admin': user.is_superuser,
            'first_name': user.first_name,
            'middle_name': user.middle_name,
            'last_name': user.last_name,
            'addresses': addresses,
            'numbers': numbers,
            'orders': orders
        })
